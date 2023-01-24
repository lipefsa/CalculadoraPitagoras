window.onload = function (){
    document.getElementById("submitButton").onclick = function (){

        a = document.getElementById("TextA").value;

        b = document.getElementById("TextB").value;
        
        //Executo o fetch que faz a requisição para a API e atualizo o HTML com o resultado
        fetch(`https://lipefsa.github.io/CalculadoraPitagoras/:5000/api?a=${a}&b=${b}`)
            .then(response => response.text())
            .then(data => {
                document.getElementById("LadoC").innerHTML = `Lado C: ${data}`;
            })
    }
}