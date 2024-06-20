function showCatalog() {
    document.getElementById("catalog").style.display = "block";
    document.getElementById("cart").style.display = "none";
    document.getElementById("statistics").style.display = "none";
}

function showCart() {
    document.getElementById("catalog").style.display = "none";
    document.getElementById("cart").style.display = "block";
    document.getElementById("statistics").style.display = "none";
}

function showStatistics() {
    document.getElementById("catalog").style.display = "none";
    document.getElementById("cart").style.display = "none";
    document.getElementById("statistics").style.display = "block";
}
