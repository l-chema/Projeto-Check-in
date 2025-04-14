document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("dark-mode-toggle");
    const body = document.body;

    if (!toggleButton) {
        console.warn("Botão de alternância de tema não encontrado!");
        return;
    }

    // Verifica o estado salvo e aplica o tema
    const darkModeEnabled = localStorage.getItem("dark-mode") === "enabled";
    body.classList.toggle("dark-mode", darkModeEnabled);
    toggleButton.textContent = darkModeEnabled ? "☀️ Modo Claro" : "🌙 Modo Escuro";

    // Alternar tema ao clicar no botão
    toggleButton.addEventListener("click", function () {
        const isDarkMode = body.classList.toggle("dark-mode");
        localStorage.setItem("dark-mode", isDarkMode ? "enabled" : "disabled");
        toggleButton.textContent = isDarkMode ? "☀️ Modo Claro" : "🌙 Modo Escuro";
    });
});
