/* reading data from jsonFile */
function readTextFile(file){
    var allText;
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function(){
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                allText = rawFile.responseText;
            }
        }
    };
    rawFile.send(null);
    return allText;
}

var jsonText = readTextFile('association_rules.json');
var jsonObj = JSON.parse(jsonText);


/* handling autocomplete */
var tokens = ['tomato', 'potato'];

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
document.getElementById('resultsDiv').style.visibility = 'hidden';
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
function getElementsSubmitted(submittedForm){
    var count = 0;
    var validElements = [];
    for (var i = 0; i < submittedForm.elements.length - 2; i++){
        if(submittedForm.elements[i].value !== ''){
            count += 1;
            validElements.push(submittedForm.elements[i].value.toLowerCase().trim());
        }
    }
    return {_count: count, _validElements: validElements};
}

function handleEmptyForm(){
    document.getElementById('ingredientsForm').style.display = 'none';
    document.getElementById('resultsDiv').style.visibility = 'visible';

    // showing a message for the empty form
    var table = document.getElementById('resultsTable');
    var row = document.createElement('tr');
    table.appendChild(row);
    var col = document.createElement('td');
    row.appendChild(col);
    col.innerHTML = 'Please give us a clue! add at least one ingredient to the search';
    var row2 = document.createElement('tr');
    table.appendChild(row2);
    var col2 = document.createElement('td');
    row2.appendChild(col2);
    var backToSearchButton = document.createElement('button');
    backToSearchButton.setAttribute('id', 'backToSearch');
    backToSearchButton.innerHTML = 'Back to search';
    // var backToSearchButton = document.getElementById('backToSearch');
    backToSearchButton.onclick = function(){
        document.getElementById('ingredientsForm').style.display = 'block';
        document.getElementById('resultsDiv').style.visibility = 'hidden';
        table.removeChild(row);
        table.removeChild(row2);
    };
    col2.appendChild(backToSearchButton);

    return false;
}

function getStringFromIngsList(sortedX){
    var XString = '';
    XString += sortedX[0];
    var i;
    for(i = 1; i < sortedX.length; i++){
        XString += ' ' + sortedX[i];
    }
    return XString;
}


function getIngredientsToAdd(ingredientsList){
    // iterating over all ingredients and the association rules that can be related to them
    var i, j, k, y, interest, ruleNum, recipeName, recipeUrl, recipeImg;
    var ingsToAdd = {};
    var allRules = [];
    var X = [];
    var sortedX, XString;
    for (i = 0; i < ingredientsList.length; i++){
        X.push(ingredientsList[i]);
        sortedX = X;
        sortedX.sort();
        XString = getStringFromIngsList(sortedX);
        // is there an association rule based on this ingredient?
        if(jsonObj.hasOwnProperty(XString)){
            // yes! insert relevant rules
            allRules = jsonObj[XString];
            for (ruleNum = 0; ruleNum < allRules.length; ruleNum++){
                y = allRules[ruleNum][0];
                if(ingredientsList.indexOf(y) > -1){
                    // we don't want to recommend something he already put in
                    continue;
                }
                interest = allRules[ruleNum][1];
                recipeName = allRules[ruleNum][2];
                recipeUrl = allRules[ruleNum][3];
                recipeImg = allRules[ruleNum][4];

                if(ingsToAdd.hasOwnProperty(y)){
                    ingsToAdd[y][0] += interest;
                    ingsToAdd[y][1] = recipeName;
                    ingsToAdd[y][2] = recipeUrl;
                    ingsToAdd[y][3] = recipeImg;
                }
                else{
                    ingsToAdd[y] = [interest, recipeName, recipeUrl, recipeImg];
                }
            }
        }

        for (j = i+1; j < ingredientsList.length; j++){
            X.push(ingredientsList[j]);
            sortedX = X;
            sortedX.sort();
            XString = getStringFromIngsList(sortedX);
            // is there an association rule based on this ingredient?
            if(jsonObj.hasOwnProperty(XString)) {
                // yes! insert relevant rules
                allRules = jsonObj[XString];
                for (ruleNum = 0; ruleNum < allRules.length; ruleNum++) {
                    y = allRules[ruleNum][0];
                    if (ingredientsList.indexOf(y) > -1) {
                        continue;
                    }
                    interest = allRules[ruleNum][1];
                    recipeName = allRules[ruleNum][2];
                    recipeUrl = allRules[ruleNum][3];
                    recipeImg = allRules[ruleNum][4];
                    if (ingsToAdd.hasOwnProperty(y)) {
                        ingsToAdd[y][0] += interest;
                        ingsToAdd[y][1] = recipeName;
                        ingsToAdd[y][2] = recipeUrl;
                        ingsToAdd[y][3] = recipeImg;
                    }
                    else {
                        ingsToAdd[y] = [interest, recipeName, recipeUrl, recipeImg];
                    }
                }
            }

            for (k = j+1; k < ingredientsList.length; k++){
                X.push(ingredientsList[k]);
                sortedX = X;
                sortedX.sort();
                XString = getStringFromIngsList(sortedX);
                // is there an association rule based on this ingredient?
                if(jsonObj.hasOwnProperty(XString)) {
                    // yes! insert relevant rules
                    allRules = jsonObj[XString];
                    for (ruleNum = 0; ruleNum < allRules.length; ruleNum++) {
                        y = allRules[ruleNum][0];
                        if (ingredientsList.indexOf(y) > -1) {
                            continue;
                        }
                        interest = allRules[ruleNum][1];
                        recipeName = allRules[ruleNum][2];
                        recipeUrl = allRules[ruleNum][3];
                        recipeImg = allRules[ruleNum][4];
                        if (ingsToAdd.hasOwnProperty(y)) {
                            ingsToAdd[y][0] += interest;
                            ingsToAdd[y][1] = recipeName;
                            ingsToAdd[y][2] = recipeUrl;
                            ingsToAdd[y][3] = recipeImg;
                        }
                        else {
                            ingsToAdd[y] = [interest, recipeName, recipeUrl, recipeImg];
                        }
                    }
                }
                X.pop();
            }
            X.pop();
        }
        X.pop();
    }
    return ingsToAdd;
}

function handleNonEmptyForm(ingredientsList){
    // getting dictionary of all possible ingredients to add
    // the value for each ingredient is the sum of interests of the association rules it appeared in
    var ingsToAdd = getIngredientsToAdd(ingredientsList);

    // displaying results
    document.getElementById('ingredientsForm').style.display = 'none';
    document.getElementById('resultsDiv').style.visibility = 'visible';

    var table = document.createElement('table');
    table.setAttribute('id', 'resultsTable');
    document.getElementById('resultsDiv').appendChild(table);
    var row, col;
    // if no results were found
    if (Object.keys(ingsToAdd).length === 0){
        row = document.createElement('tr');
        table.appendChild(row);
        col = document.createElement('td');
        col.setAttribute('colspan','2');
        row.appendChild(col);
        col.innerHTML = 'We found nothing to add. Your recipe is probably already AWESOME!';
    }
    else{
        row = document.createElement('tr');
        table.appendChild(row);
        col = document.createElement('td');
        col.setAttribute('colspan','2');
        row.appendChild(col);
        col.innerHTML = 'We think it would be cool to add one (or more) of the following:';

        var ingredientRow, ingredientCol, recipeSpan, recipeCol;
        var innerTable, innerRow, innerCol1, innerCol2, recipeImg, recipeUrl;
        for(var ingredient in ingsToAdd){
            ingredientRow = document.createElement('tr');
            table.appendChild(ingredientRow);
            ingredientCol = document.createElement('td');
            ingredientRow.appendChild(ingredientCol);

            ingredientCol.innerHTML = ingredient;

            recipeCol = document.createElement('td');
            recipeSpan = document.createElement('span');
            recipeCol.appendChild(recipeSpan);
            recipeSpan.setAttribute('class', 'popupRecipe');
            ingredientRow.appendChild(recipeCol);

            innerTable = document.createElement('table');
            recipeSpan.appendChild(innerTable);
            innerRow = document.createElement('tr');
            innerTable.appendChild(innerRow);

            // image
            innerCol1 = document.createElement('td');
            innerRow.appendChild(innerCol1);
            recipeImg = document.createElement('img');
            recipeImg.setAttribute('class', 'recipeImage');
            if(ingsToAdd[ingredient][3] === ''){
                recipeImg.setAttribute('src', 'default-recipe.png');
            }
            else{
                recipeImg.setAttribute('src', ingsToAdd[ingredient][3]);
            }
            innerCol1.appendChild(recipeImg);

            // recipe name and url
            innerCol2 = document.createElement('td');
            recipeUrl = document.createElement('a');
            recipeUrl.setAttribute('href', ingsToAdd[ingredient][2]);
            recipeUrl.innerHTML = ingsToAdd[ingredient][1];
            innerCol2.appendChild(recipeUrl);
            innerRow.appendChild(innerCol2);
        }
    }

    // last row: button
    var lastRow = document.createElement('tr');
    table.appendChild(lastRow);
    var buttonCol = document.createElement('td');
    buttonCol.setAttribute('colspan','2');
    lastRow.appendChild(buttonCol);
    var backToSearchButton = document.createElement('button');
    backToSearchButton.setAttribute('id', 'backToSearch');
    backToSearchButton.innerHTML = 'Back to search';
    // var backToSearchButton = document.getElementById('backToSearch');
    backToSearchButton.onclick = function(){
        document.getElementById('ingredientsForm').style.display = 'block';
        document.getElementById('resultsDiv').style.visibility = 'hidden';
        document.getElementById('resultsDiv').removeChild(table);
    };
    buttonCol.appendChild(backToSearchButton);
    return false;
}

function formSubmitHandler(){
    var submittedForm = document.getElementById('ingredientsForm');
    var submittedElems = getElementsSubmitted(submittedForm);

    if(submittedElems._count === 0){
        handleEmptyForm();
    }
    else{
        handleNonEmptyForm(submittedElems._validElements);
    }
}
