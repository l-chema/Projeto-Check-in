//document.addEventListener("DOMContentLoaded", function () {
/*   const toggleButton = document.getElementById("dark-mode-toggle");
    const body = document.body;

    // Verificar se o usuário já escolheu um tema antes
    if (localStorage.getItem("dark-mode") === "enabled") {
        body.classList.add("dark-mode");
        toggleButton.textContent = "☀️ Modo Claro";
    }

    // Alternar tema ao clicar no botão
    toggleButton.addEventListener("click", function () {
        body.classList.toggle("dark-mode");

        // Salvar preferência no localStorage
        if (body.classList.contains("dark-mode")) {
            localStorage.setItem("dark-mode", "enabled");
            toggleButton.textContent = "☀️ Modo Claro";
        } else {
            localStorage.setItem("dark-mode", "disabled");
            toggleButton.textContent = "🌙 Modo Escuro";
        }
    });
}); */ 
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
