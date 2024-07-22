document.addEventListener("DOMContentLoaded", () => {
    const currentPath = window.location.pathname;

    const headerTitle = document.querySelector("header h1 a");
    const navLinks = document.querySelectorAll("nav a");

    // Hide the navigation link for the current page
    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.style.display = "none";
        }
    });

    // Update the header title based on the current page
    if (currentPath === "/") {
        headerTitle.textContent = "Personal Blog";
    } else if (currentPath === "/posts/") {
        headerTitle.textContent = "Home";
    } else {
        headerTitle.textContent = "My Blog"; // Default or based on your preference
    }
});
