function Calculer(){
    let number1 = parseFloat(document.getElementById("num1").value) ;
    let number2 = parseFloat(document.getElementById("num2").value) ;
    

        if(isNaN(number1) || isNaN(number2)){
            alert("Vueiller entrer un nombre");
        }else{
            let sum = number1 + number2;
            document.getElementById("text").innerText = "Resultat : " +sum;
            //alert("resultat : " +sum );
        }
    
}