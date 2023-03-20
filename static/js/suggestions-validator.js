console.log('Js Linked');
function validator(){
    const name = document.getElementById('name').value
    const suggestion = document.getElementById('suggestion').value
    let error = false
    console.log(name + " " + suggestion)

    if(name === ""){
        error = true
        document.getElementById('name_error').innerHTML = 'Name is required.'
        document.getElementById('name').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('name_error').innerHTML = ''
        document.getElementById('name').setAttribute("class","form-control is-valid")
    }

    if(suggestion === ""){
        error = true
        document.getElementById('suggestion_error').innerHTML = 'Suggestion is required.'
        document.getElementById('suggestion').setAttribute("class","form-control is-invalid")
    }
    else{
        document.getElementById('suggestion_error').innerHTML = ''
        document.getElementById('suggestion').setAttribute("class","form-control is-valid")
    }

    if(error){
        return false
    }
    else{
        return true
    }
}