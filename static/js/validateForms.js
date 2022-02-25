function validateDeposit(){
    var deposit_amount = document.getElementById("id_depositAmount").value;
    if(deposit_amount > 0)
        return true;
    else
        alert("Cannot deposit/withdraw negative value");
    return false;
}

function validateWithdraw(){
    var withdraw_amount = document.getElementById("id_withdrawlAmount").value;
    console.log(withdraw_amount)
    if(withdraw_amount > 0)
        return true;
    else
        alert("Cannot deposit/withdraw negative value");
    return false;
}