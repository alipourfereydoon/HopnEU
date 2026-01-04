document.addEventListener("DOMContentLoaded", () => {
    console.log("NovaIntel website loaded");
});


document.addEventListener("DOMContentLoaded", () => {
    const menuItems = document.querySelectorAll(".sidebar-menu li");

    menuItems.forEach(item => {
        item.addEventListener("click", () => {
            menuItems.forEach(i => i.classList.remove("active"));
            item.classList.add("active");
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".hero-slide");
    let current = 0;

    setInterval(() => {
        slides[current].classList.remove("active");
        current = (current + 1) % slides.length;
        slides[current].classList.add("active");
    }, 5000); // change every 5 seconds
});
