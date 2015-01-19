function sub(a,b){
	return a+b;
}

function fuc(f,a){
	return f(a,3);
}

function fuc1(){
	console.log("I am func1");
	return function(){
		console.log("hello");
		console.log("Exit func1");
	}

}

function execute(someFunction, value) {
  someFunction(value);
}
execute(function(word){ console.log(word) }, "Hello");

console.log(sub(10,3));
console.log(fuc(sub,10));
console.log(fuc1());
console.log("=============");
console.log(fuc1()());
