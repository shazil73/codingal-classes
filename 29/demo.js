// var obj = {name:"shazil zahid", age: 20, city: "karachi"}

// var j = JSON.stringify(obj)

// var obj2 = JSON.parse(j)

// console.log(j)

// document.getElementById("hello").innerHTML = obj2.name + "  " + obj2.age + "  " + obj2.city

function getVideo () {
    return new Promise ((resolve) => {setTimeout(() => {console.log("there are some video")},3000);})}


    async function showVideo () {
        await getVideo();
        console.log("video is ready");
    }
    
showVideo()
console.log("i print first")
