/* handling autocomplete */
var tokens = ['tomato', 'potato'];
// var dbHandler = require('dbHandler.js');

function addAutoComplete(inputFieldNum){
    var ing = document.getElementById('ingredient'+inputFieldNum);
    var thisAwesomplete = new Awesomplete(ing, {
        autoFirst: true,
        maxItems: 10,
        list: tokens
    });
}

/* handling startButton */
document.getElementById('ingredientsForm').style.visibility = 'hidden';
var startButton = document.getElementById('startButton');
startButton.onclick = function(){
    document.getElementById('ingredientsForm').style.visibility = 'visible';
    for(var i = 1; i < 4; i++){
        addAutoComplete(i);
    }
    startButton.style.display = 'none';
};

/* handling addition of extra ingredients to the form */
var inputFieldsCounter = 4;

var addInputButton = document.getElementById('addIngredientInputButton');
addInputButton.onclick = function(){
    var newListItem = document.createElement('li');
    var newInputLabel = document.createElement('label');
    newInputLabel.innerHTML = "Ingredient #"+inputFieldsCounter+": ";

    var newInputField = document.createElement('input');
    newInputField.setAttribute('type', 'text');
    newInputField.setAttribute('class', 'awesomplete');
    newInputField.setAttribute('id', 'ingredient'+inputFieldsCounter);
    newInputField.setAttribute('placeholder', 'Type ingredient here');

    newListItem.appendChild(newInputLabel);
    newListItem.appendChild(newInputField);
    document.getElementById("form-list").appendChild(newListItem);
    addAutoComplete(inputFieldsCounter);

    inputFieldsCounter += 1;
    return false;
};

/* handling form submit */
function countElementsSubmitted(submittedForm){
    var count = 0;
    for (var i = 0; i < submittedForm.elements.length - 2; i++){
        if(submittedForm.elements[i].value !== ''){
            count += 1;
        }
    }
    return count;
}

function handleEmptyForm(){
    document.write('you submitted an empty form');
    return false;
}

function formSubmitHandler(){
    var submittedForm = document.getElementById('ingredientsForm');
    var countSubmittedIngredients = countElementsSubmitted(submittedForm);

    if(countSubmittedIngredients === 0){
        handleEmptyForm();
    }
    else{
        document.write('you submitted a form with '+countSubmittedIngredients+' ingredients');
        return false;
    }
}