var shazil = {
    america: "New York", india: "Delhi", pakistan: "Lahore", d: function (a, b) {
        return Math.pow(a, b)
    }
}
console.log(shazil.america);
console.log(shazil.india);
console.log(shazil.pakistan);
console.log(shazil.d(2, 3));

console.log(Math.random())
var shazil2 = ['hashim', 'ayyan', 'asad', 'saad',];

console.log(shazil2[0])
console.log(shazil2[1])
console.log(shazil2[2])

console.log(shazil2.shift())
console.log(shazil2)

console.log(shazil2.join('...'))

function add(a, b) {
    return a + b;
}
function average(a, b) {
    return add(a, b) / 2
}

console.log(average(10, 20))

