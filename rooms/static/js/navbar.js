// console.log(document.title)
switch(document.title){
    case "Home":
        document.getElementById("home").classList.add("active");
        break
    case "Status":
        document.getElementById("status").classList.add("active");
        break
    case "Rooms":
        document.getElementById("rooms").classList.add("active");
        break
    case "Application":
        document.getElementById("application").classList.add("active");
        break
    case "Contat Us":
        document.getElementById("contact").classList.add("active");
}