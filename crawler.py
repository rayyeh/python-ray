#! /usr/bin/env python
#  Copyright (C) 2009  Veronica Valeros
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#
# Author:
# Veronica Valeros vero.valeros@gmail.com
#
# Changelog
# - Almost all from the last published version! 

# standar imports
import sys
import re
import getopt
import urllib2
import urlparse
import httplib
import copy
import os
import time
import socket
import datetime

import getpass

####################
# Global Variables
debug=False
vernum='1.0'
verbose=False
log=False
auth=False

log_file = ""
links_crawled=[]
files=[]
crawl_limit_flag = False
output=""
output_name=""

# This is for identify links in a HTTP answer
#linkregex = re.compile('[^>](?:href=|src=|content=\"http)[\'*|\"*](.*?)[\'|\"]',re.IGNORECASE)
linkregex = re.compile('[^>](?:href\=|src\=|content\=\"http)[\'*|\"*](.*?)[\'|\"].*?>',re.IGNORECASE)
linkredirect = re.compile('(?:open\\(\"|url=|URL=|location=\'|src=\"|href=\")(.*?)[\'|\"]')
linksrobots = re.compile('(?:Allow\:|Disallow\:|sitemap\:).*',re.IGNORECASE)
information_disclosure = re.compile('(?:<address>)(.*)[<]',re.IGNORECASE)


# HTTP Response Codes
# -------------------
error_codes={}
error_codes['0']='Keyboard Interrupt exception'
error_codes['1']='Skypping url'
error_codes['-2']='Name or service not known'
error_codes['22']='22 Unknown error'
error_codes['104']='104 Connection reset by peer'
error_codes['110']='110 Connection timed out'
error_codes['111']='111 Connection refused'
error_codes['200']='200 OK'
error_codes['300']='300 Multiple Choices'
error_codes['301']='301 Moved Permanently'
error_codes['302']='Moved'
error_codes['305']='305 Use Proxy'
error_codes['307']='307 Temporary Redirect'
error_codes['400']='400 Bad Request'
error_codes['401']='401 Unauthorized'
error_codes['403']='403 Forbidden'
error_codes['404']='404 Not Found'
error_codes['405']='405 Method Not Allowed'
error_codes['407']='407 Proxy Authentication Required'
error_codes['408']='408 Request Timeout'
error_codes['500']='500 Internal Server Error'
error_codes['503']='503 Service Unavailable'
error_codes['504']='504 Gateway Timeout'
error_codes['505']='505 HTTP Version Not Supported'
error_codes['9999']='Server responds with a HTTP status code that we do not understand'


# End of global variables
###########################


# Print version information and exit
def version():
	"""
	This function prints the version of this program. It doesn't allow any argument.
	"""
	print "+----------------------------------------------------------------------+"
    	print "| "+ sys.argv[0] + " Version "+ vernum +"                                      |"
	print "| This program is free software; you can redistribute it and/or modify |"
	print "| it under the terms of the GNU General Public License as published by |"
	print "| the Free Software Foundation; either version 2 of the License, or    |"
	print "| (at your option) any later version.                                  |"
	print "|                                                                      |"
	print "| Author: Veronica Valeros, vero.valeros@gmail.com                     |"
	print "+----------------------------------------------------------------------+"
	print

# Print help information and exit:
def usage():
	"""
	This function prints the posible options of this program.
	"""
	print "+----------------------------------------------------------------------+"
	print "| "+ sys.argv[0] + " Version "+ vernum +"                                      |"
	print "| This program is free software; you can redistribute it and/or modify |"
	print "| it under the terms of the GNU General Public License as published by |"
	print "| the Free Software Foundation; either version 2 of the License, or    |"
	print "| (at your option) any later version.                                  |"
	print "|                                                                      |"
	print "| Author: Veronica Valeros, vero.valeros@gmail.com                     |"
	print "+----------------------------------------------------------------------+"
	print 
	print "\nUsage: %s <options>" % sys.argv[0]
	print "Options:"
    	print "  -h, --help                           Show this help message and exit"
      	print "  -V, --version                        Output version information and exit"
	print "  -v, --verbose                        Be verbose"
        print "  -D, --debug                          Debug"
	print "  -u, --url                            URL to start crawling"
        print "  -L, --common-log-format              Generate log of the requests in CLF"
        print "  -U, --usuario                        User name for authentication"
        print "  -P, --password                       Request password for authentication"
        print "  -l, --crawl-limit                    Maximum links to crawl"
	print "  -d, --download-file                  Specify the file type of the files to download: png,pdf,jpeg,gif,css,x-javascript,x-shockwave-flash"
        print "  -i, --interactive-download           Before downloading files allow user to specify manually the type of files to download"
        print "  -e, --export-file-list               Creates a file with all the URLs to found files during crawling. You can use wget to download the entire list"
	print
	print "Example: python crawler.py -u http://www.example.com"
	print
	sys.exit(1)

def printout(text):
	global debug
	global verbose
	global output

	try:
		print text 
		output.write(text+'\n')

        except Exception as inst:
		print '[!] Exception in printout() function'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1


def check_url(url):
	global debug
	global verbose

	try:
		url_parsed = urlparse.urlparse(url)
		if url_parsed.scheme and url_parsed.netloc:
			return True
		else:
			return False

        except Exception as inst:
		print '[!] Exception in check_url() function'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1

def encode_url(url):
	global debug
	global verbose

	url_encoded = ""
	try:	
		url_encoded = url.replace(" ","%20")
		url_encoded = url.replace("&amp;","&")
		
		return url_encoded
        except Exception as inst:
		print '[!] Exception in encode_url() function'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return False

def log_line(request, response_code, response_size):
	global log_file

	try:
		if response_size == -1:
			content_size = '-'
		else:
			content_size = str(response_size)
		local_hostname = socket.gethostname()
		local_user = os.getenv('USER')
		timestamp = time.strftime('%e/%b/%Y:%X %z').strip()
		method = request.get_method()
		protocol = 'HTTP/1.1'	# This is the version of the protocol that urllib2 uses
		user_agent = request.get_header('User-agent')
		url = request.get_full_url()
		
		# COMMON LOG FORMAT
		log_file.write(local_hostname+' '+'-'+' '+local_user+' '+'['+timestamp+']'+' '+'"'+method+' '+url+' '+protocol+'"'+' '+str(response_code)+' '+content_size+' "-" "'+user_agent+'"\n')

		# URLSNARF FORMAT
		#log_file.write(local_hostname+' '+'- - '+'['+timestamp+']'+' '+'"'+method+' '+url+' '+protocol+'"'+' - - "-" "'+user_agent+'"\n')
	except Exception as inst:
		print '[!] Exception in log_line() function'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y

def get_url(url, host, username, password):
	global debug
	global verbose
	global log
	global auth


	try:
		try:
			url = encode_url(url)
			request = urllib2.Request(url)
			request.add_header('User-Agent','Mozilla/4.0 (compatible;MSIE 5.5; Windows NT 5.0)')

			if auth:
				password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
				password_manager.add_password(None, host, username, password)
				handler = urllib2.HTTPBasicAuthHandler(password_manager)

				opener_web = urllib2.build_opener(handler)
			else: 
				opener_web = urllib2.build_opener()


			response = opener_web.open(request)

			opener_web.close()

			return [request,response]


                except urllib2.HTTPError,error_code:
			return [request,error_code.getcode()]
		except urllib2.URLError,error_code:
			error = error_code.args[0]
			return [request,error[0]]
		except socket.error,error_code:
			error = error_code.args[0]
			try:
				error = error[0]
			except:
				pass
			return [request,error]
			
	except KeyboardInterrupt:
		try:
			print '\t[!] Press a key to continue' 
			raw_input()
			return ["",1]
		except KeyboardInterrupt:
			return ["",0]
        except Exception as inst:
		print '[!] Exception in get_url() function'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1	

def get_links(link_host, link_path, content):
	global debug
	global verbose
	global linkregex

	try:
		# We obtain the links in the given response
		links = linkregex.findall(content)

		# We analyze each link 
		for link in links:
			try:
				link_clean = link.strip(' ')
			except:
				print 'error'
			parsed_link = urlparse.urlparse(link_clean)
			if not parsed_link.scheme and not parsed_link.netloc:
				if link_clean.startswith('/'):
					if link_host.endswith('/'):
						links[links.index(link)] = link_host.rstrip('/')+link_clean
					else:
						links[links.index(link)] = link_host+link_clean
				elif link_clean.startswith('./'):
						links[links.index(link)] = link_host+link_clean
				else:
					links[links.index(link)] = link_path+link_clean
			else:
				links[links.index(link)] = link_clean

		return links

        except Exception as inst:
		print '[!] Exception in get_links() function'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1

def crawl(url,usuario,password,crawl_limit):
	global debug
	global verbose
	global error_codes
	global log_file
	global log
	global links_crawled
	global crawl_limit_flag
	global output_name
	global files
	
	
	FLAG = True

	# We save the main URL for later usage
	main_url = url

	# Vector that stores the remaining URLs to crawl
	urls_to_crawl = []
	urls_not_crawled = []
	links_crawled = []
	links_extracted = []
	date = str(datetime.datetime.today()).rpartition('.')[0].replace('-','').replace(' ','_').replace(':','')
	filename = date +'_'+ urlparse.urlparse(url).netloc + '.log'


	urls_to_crawl.append(url)
	try:
		if log:
			try: 
				log_file = open(filename,'w')
			except:
				print '[!] Imposible to create the output log file'


		printout('[+] Site to crawl: '+url)
		printout('[+] Start time: '+str(datetime.datetime.today()))
		printout('[+] Output file: '+output_name)
		if log:
			printout('[+] Common log format output: '+filename)
		printout('')

		printout('[+] Crawling')

		while urls_to_crawl:
			if crawl_limit_flag:
				if (len(links_crawled) >= crawl_limit):
					break
			try:
				# We extract the next url to crawl
				url = urls_to_crawl[0]
				urls_to_crawl.remove(url)

				# We add the url to the links crawled
				links_crawled.append(url)

				# We print the URL that is being crawled
				printout('   [-] '+url)

				# We extract the host of the crawled URL	
				parsed_url = urlparse.urlparse(url)
				host = parsed_url.scheme + '://' + parsed_url.netloc

				if parsed_url.path.endswith('/'):
					link_path = host + parsed_url.path
				else:
					link_path = host + parsed_url.path.rpartition('/')[0] + '/'

				# We obtain the response of the URL
				[request,response] = get_url(url,host,usuario, password)

				# If there is a response
				if response:
					#If the server didn't return an HTTP Error
					if not isinstance(response, int):
						content = response.read()

						if log:
							log_line(request,response.getcode(),len(content))

						# We print the file type of the crawled page
						if response.headers.typeheader:
							# If it isn't an HTML file
							if 'text/html' not in response.headers.typeheader:
								if url not in files:
									files.append([url,response.headers.typeheader])
								if verbose:
									printout('\t[-] ('+str(response.getcode())+') '+str(response.headers.typeheader))
							else:
								if verbose:
									printout('\t[-] ('+str(response.getcode())+') '+str(response.headers.typeheader))

								links_extracted = get_links(host, link_path, content)
								links_extracted.sort()

								# We add new links to the list of urls to crawl
								for link in links_extracted:
									if debug:
										print '\t   [i] {0}'.format(link)
									parsed_link= urlparse.urlparse(link)
									link_host = parsed_link.scheme + '://' + parsed_link.netloc

									# We just crawl URLs of the same host
									if link_host == host:
										if link not in links_crawled and link not in urls_to_crawl:
											urls_to_crawl.append(link)
									elif link not in urls_not_crawled:
										urls_not_crawled.append(link)
					else:
						# We print the error code if neccesary
						printout('\t[i] '+error_codes[str(response)])
						if log:
							log_line(request,response,-1)
				else:
					if response==1:
						continue
					if response==0:
						print '[!] Skypping the rest of the urls'
						break

			except KeyboardInterrupt:
				try:
					print '[!] Press a key to continue' 
					raw_input()
					continue
				except KeyboardInterrupt:
					print '[!] Exiting'
					break	

			except Exception as inst:
				print '[!] Exception inside crawl() function. While statement rise the exception.'
				print type(inst)     # the exception instance
				print inst.args      # arguments stored in .args
				print inst           # __str__ allows args to printed directly
				x, y = inst          # __getitem__ allows args to be unpacked directly
				print 'x =', x
				print 'y =', y
				print 'Response: {0}'.format(response)
				break
		
		if log:
			log_file.close()
		printout('[+] Total urls crawled: '+str(len(links_crawled)))
		printout('')
		printout('[+] Output file stored at: '+os.path.abspath(output_name))
		printout('')

	except KeyboardInterrupt:
		try:
			print '[!] Press a key to continue' 
			raw_input()
			return 1
		except KeyboardInterrupt:
			print '[!] Keyboard interruption. Exiting'
			return 1
       
	except Exception as inst:
		print '[!] Exception in crawl() function'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1

def indexing_search(usuario, password):
	global debug
	global verbose
	global links_crawled
	global error_codes

	directories=[]
	indexing=[]
	request=""
	response=""

	title_start_position = -1
	title_end_position = -1
	title=""

	try:

		# Identifying directories
		for i in links_crawled:
			while ( len(i.split('/')) > 4 ):
				i=i.rpartition('/')[0]
				if ( ( i+'/' )  not in directories ):
					directories.append(i+'/')

		# We sort the directories vector for proper visualization of the data
		directories.sort()
		
		printout('[+] Directories found:')
		for directory in directories:
			printout('   [-] '+directory)
		printout('[+] Total directories: '+str(len(directories)))
		printout('')

		printout('[+] Directory with indexing')
		for directory in directories:
			try:
				# We extract the host of the crawled URL	
				parsed_url = urlparse.urlparse(directory)
				host = parsed_url.scheme + '://' + parsed_url.netloc
				
				# We obtain the response of the URL
				[request,response] = get_url(directory, host, usuario, password)		

				# If there is a response                                			
				if response:
					#If the server didn't return an HTTP Error      		
					if not isinstance(response, int):
						content = response.read()

						title_start_position = content.find('<title>')
						if title_start_position != -1:
							title_end_position = content.find('</title>', title_start_position+7)
						if title_end_position != -1:
							title = content[title_start_position+7:title_end_position]

						if title:
							if title.find('Index of') != -1:
								printout('   [!] '+directory)
								indexing.append(directory)

					else:
						if debug:
							# We print the error code if neccesary
							printout('   [-] '+directory+' ('+error_codes[str(response)]+')')
				else:
					if response==1:
						continue
					if response==0:
						print '[!] Skypping the rest of the directories'
						break
			except KeyboardInterrupt:
				try:
					print '[!] Press a key to continue' 
					raw_input()
					pass
				except KeyboardInterrupt:
					print '[!] Exiting'
					break	

		printout('[+] Total directories with indexing: '+str(len(indexing)))
		printout('')

	except Exception as inst:
		print '[!] Exception in indexing_search() function'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return 1

def report_files(export_file_list):
	global debug
	global verbose
	global files
	global output_name

	try:
		if len(files)>0:
			printout('[+] Files found:')
			if export_file_list:
				try:
					local_file = open(output_name.rpartition('.')[0]+'.files','w')
				except OSError,error:
					if 'File exists' in error:
						pass
					else:
						print '[+] Error creating output file to export list of files.'
						export_file_list=False

			if export_file_list:
				printout('[+] Exporting list of files found to: '+output_name.rpartition('.')[0]+'.files')
			# We print the files found during the crawling
			for [i,j] in files:
				printout('   [-] '+i+'  ('+j+')')
				if export_file_list:
					local_file.write(i+'\n')
			printout('[+] Total files: '+str(len(files)))

	except Exception as inst:
		print '[!] Exception in report_files() function'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return 1

def download_files(files_to_download,usuario,password,interactive_flag):
	global debug
	global verbose
	global files
	global output_name

	list_of_files_to_download=[]
	type_of_files=[]

	try:
		if len(files)>0:
			# Looking for the types of files found during crawling	
			for [i,j] in files:
				if j.split('/')[1].split(';')[0] not in type_of_files:
					type_of_files.append(j.split('/')[1].split(';')[0] )

			#If the interactive mode is enabled, we ask user which files to downlaod
			if interactive_flag:
			 	print	
				print '[+] Starting to download files'
				print '[+] The following files were found during crawling:'
				print '   ',
				print type_of_files
				print '    Select next wich type of files you want to download. Ex.: png,pdf,css.'
				files_to_download= raw_input('    ')

			# Looking for files matching the download criteria	
			for [i,j] in files:
				if (j.split('/')[0].split(';')[0] in files_to_download) or (j.split('/')[1].split(';')[0] in files_to_download):
					list_of_files_to_download.append(i)	

			# If there is at least one file matching the download criteria, we create a output directory and download them
			if ( len(list_of_files_to_download) > 0 ):
				# Fetching found files
				printout('')
				printout('[+] Downloading specified files: '+files_to_download)
				printout('[+] Total files to download: '+str(len(list_of_files_to_download)))

				# Creating output directory download files
				try:
					output_directory = output_name.rpartition('.')[0]+'_files'
					os.mkdir(output_directory)
					printout('[+] Output directory: '+output_directory)
				except OSError, error:
					if 'File exists' in error:
						print '\n[!] Directory already exists. Press a key to ovewrite or CTRL+C cancel download'
						try:
							raw_input()
							printout('[+] Output directory: '+output_directory)
						except KeyboardInterrupt:
							printout('\n[+] Download files aborted')
							return 1 
					else:
						printout('\n[!] Download files aborted. Error while creating output directory.')


				#Downloading files
				for i in list_of_files_to_download:
					printout('   [-] '+i)

					# We extract the host of the crawled URL	
					parsed_url = urlparse.urlparse(i)
					host = parsed_url.scheme + '://' + parsed_url.netloc

					[request,response] = get_url(i.replace(' ','%20'), host, usuario, password)		

					if response:
						try:
							local_file=open(output_directory+'/'+i.rpartition('/')[2],'w')
						except OSError, error:
							if 'File exists' in error:
								pass
							else:
								printout('   [-] Impossible to create output file for: '+output_directory+'/'+i.rpartition('/')[2])

						local_file.write(response.read())
						local_file.close()

			printout('[+] Download complete')
			printout('')
					


	except Exception as inst:
		print '[!] Exception in download_files() function'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1



##########
# MAIN
##########
def main():

	global debug
	global verbose
	global log
	global auth
	global crawl_limit_flag
	global output
	global output_name

	url_to_crawl = ""
	usuario = "crawler123"
	password = "crawler123"
	crawl_limit = 0
	files_to_download = "" 
	download_files_flag=False
	export_file_list = False
	interactive_flag=False

	try:

		# By default we crawl a max of 5000 distinct URLs
		opts, args = getopt.getopt(sys.argv[1:], "hVDu:vLU:Pl:[d:]ei", ["help","version","debug","url=","verbose","common-log-format","usuario=","password","crawl-limit=","[download-file=]","export-file-list","interactive-download"])


	except getopt.GetoptError: usage()	

	for opt, arg in opts:
		if opt in ("-h", "--help"): usage()
		if opt in ("-V", "--version"): version();exit(1)
		if opt in ("-D", "--debug"): debug=True
		if opt in ("-u", "--url"): url_to_crawl = arg
		if opt in ("-v", "--verbose"): verbose = True
		if opt in ("-L", "--common-log-format"): log = True
		if opt in ("-U", "--usuario"): usuario = arg
		if opt in ("-P", "--password"): password = getpass.getpass() ; auth = True
		if opt in ("-l", "--crawl-limit"): crawl_limit = int(arg) ; crawl_limit_flag = True 
		if opt in ("-d", "--download-file"): files_to_download = arg ; download_files_flag=True
		if opt in ("-i", "--interactive-download"): interactive_flag=True
		if opt in ("-e", "--export-file-list"): export_file_list = True
	try:

		if debug:
			print '[+] Debugging mode enabled'

		if check_url(url_to_crawl):
			try:
				output_name = urlparse.urlparse(url_to_crawl).netloc + '.crawler'
				output = open(output_name,'w')
			except:
				print '[!] Not saving data in output' 

			crawl(url_to_crawl, usuario, password, crawl_limit)
			
			indexing_search(usuario, password)
			
			report_files(export_file_list)
			
			if download_files_flag or interactive_flag:
				download_files(files_to_download,usuario,password,interactive_flag)
			
			
			printout('[+] End time: '+str(datetime.datetime.today()))

			try:
				output.close()
			except:
				pass

		else:
			print
			print '[!] Check the URL provided, it should be like: http://www.example.com or http://asdf.com'
			print
			usage()

	except KeyboardInterrupt:
		# CTRL-C pretty handling
		print 'Keyboard Interruption!. Exiting.'
		sys.exit(1)


if __name__ == '__main__':
	main()
