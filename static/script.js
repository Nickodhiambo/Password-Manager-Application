const { inputs } = document.querySelectorAll("input")
const copyButtons = document.querySelectorAll("span#copy");

const updateInputs = (inputs) => {
    inputs.forEach((i, index) => {
        const copiedText = i.value[index];
        navigator.clipboard.writeText(copiedText);
    });
};

copyButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        updateInputs([...inputs]);
        btn.textContent = "d";
        setTimeout(() => btn.textContent = "c", 1000);
    });
});