var a = 6  // number
var b = 7.6  // number
var c = null  // object
var d = "Hello, World!"  //string
var e = undefined  // undefined
var f = true  //boolean
var g = false  //boolean
var h = {color: "red", size: 10, shape: "circle"}  // object

console.log(a);
console.log(b);
console.log(c);
console.log(d);
console.log(e);
console.log(f);
console.log(g);
console.log(h);
console.log(typeof(a));

var i = 'shazil'
console.log(i);

try{
   var j = 50 / 0
    console.log(j);
    var k = 0 / 50
    console.log(k);
    throw new Error("This is an error message");
}catch(err) {
    console.log(err.message);
    console.log("An error occurred");
}

function greet(){
    console.log("Hello");
    console.log("how are you?");
    console.log("I am fine");
}
greet();

var shazil = (a)=> {console.log("I am shazil",a)};
var shazil2 = (b) => {console.log("my name is shazil zahid",b)};
shazil("thanks")
shazil2("thanks2")

