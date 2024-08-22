const params = new URLSearchParams(window.location.search);
const name = params.get("filepath")
const player = document.querySelector("#video")
player.src = name
// console.log(name)