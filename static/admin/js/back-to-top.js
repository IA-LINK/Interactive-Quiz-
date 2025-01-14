const backToTopButton = document.createElement("div");
backToTopButton.classList.add("back-to-top");
backToTopButton.innerHTML = "↑";
document.body.appendChild(backToTopButton);

backToTopButton.addEventListener("click", function() {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

window.addEventListener("scroll", function() {
    if (window.scrollY > 300) {
        backToTopButton.style.display = "block";
    } else {
        backToTopButton.style.display = "none";
    }
});
