/* constants for the program */
var OVERALL_INTEREST = 0;
var RECIPE_SPECIFIC_INTEREST = 1;
var RECIPE_NAMES = 2;
var RECIPE_URLS = 3;
var RECIPE_IMGS = 4;
var NUM_INGREDIENTS_TO_DISPLAY = 4;
var JSON_ALL = 'all_association_rules.json';
var JSON_APPETIZERS = 'appetizers_association_rules.json';
var JSON_DESERTS = 'deserts_association_rules.json';
var JSON_DRINKS = 'drinks_association_rules.json';
var JSON_EASY = 'easy_association_rules.json';
var JSON_ITALIAN = 'italian_association_rules.json';
var JSON_MEAT = 'meat_and_poultry_association_rules.json';
var JSON_SALAD = 'salad_association_rules.json';
var JSON_SOUP = 'soups_stews_chili_association_rules.json';

var jsonObj; //to be filled later with the relevant path

/* setting display */
document.getElementById('ingredientsForm').style.visibility = 'hidden';
document.getElementById('resultsDiv').style.visibility = 'hidden';
document.getElementById('mainHeaderImg').style.visibility = 'hidden';

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

var tokens = ["bacon", "spinach", "parsley", "spray", "sherry", "carrot", "pineapple", "lime", "onions", "honey", "seasoning", "dill", "raisins", "paprika", "salt", "onion", "vanilla", "cornstarch", "scallions", "rosemary", "turmeric", "vodka", "garlic", "chives", "nutmeg", "ginger", "carrots", "flour", "ice", "margarine", "buttermilk", "half-and-half", "beef", "mustard", "cilantro", "cumin", "walnuts", "almonds", "pumpkin", "tarragon", "cream", "peas", "tomatoes", "mayonnaise", "chicken", "thyme", "lemon", "tomato", "molasses", "pepper", "butter", "apples", "shallots", "strawberries", "basil", "milk", "mushrooms", "allspice", "eggs", "almond", "parmesan", "orange", "bananas", "capers", "raspberries", "pork", "essence", "blueberries", "shallot", "cinnamon", "pecans", "sugar", "cayenne", "zucchini", "egg", "sage", "ketchup", "avocado", "cranberries", "potatoes", "shortening", "coriander", "oil", "celery", "cornmeal", "water", "oregano", "mint", "green onion", "yellow onion", "canola oil", "egg whites", "flat-leaf parsley", "parmesan cheese", "warm water", "garlic salt", "shrimp deveined", "orange juice", "red onion", "sea salt", "brown sugar", "stalks celery", "egg yolks", "baking soda", "chicken breasts", "black beans", "red wine", "chili powder", "tomato sauce", "stalk celery", "lean beef", "peanut oil", "whipping cream", "flour dusting", "egg yolk", "white onion", "sweet potatoes", "beef broth", "corn syrup", "rolled oats", "boiling water", "white pepper", "plain yogurt", "white rice", "confectioners sugar", "white vinegar", "stick butter", "mint leaves", "powdered sugar", "cilantro leaves", "whipped topping", "wheat flour", "hot sauce", "chicken stock", "balsamic vinegar", "tomato paste", "sour cream", "thyme leaves", "unsalted butter", "cream tartar", "green onions", "bread crumbs", "ginger root", "white wine", "black olives", "yellow onions", "garlic smashed", "black peppercorns", "active yeast", "rosemary leaves", "cider vinegar", "curry powder", "parsley leaves", "maple syrup", "cayenne pepper", "lime juice", "soy sauce", "vegetable oil", "cheddar cheese", "garlic powder", "dijon mustard", "lime juiced", "evaporated milk", "lemon juiced", "sesame oil", "juice lemon", "chicken broth", "bay leaves", "mozzarella cheese", "cream cheese", "bay leaf", "lemon juice", "chicken breast", "olive oil", "cherry tomatoes", "granulated sugar", "red pepper", "black pepper", "hot water", "rice vinegar", "pineapple juice", "baking powder", "coconut milk", "worcestershire sauce", "green beans", "onion powder", "salt pepper", "basil leaves", "white sugar", "peanut butter", "cracked black pepper", "white wine vinegar", "dark brown sugar", "low-sodium chicken broth", "red wine vinegar", "monterey jack cheese", "salt black pepper", "apple cider vinegar", "unsweetened cocoa powder", "semisweet chocolate chips", "sticks unsalted butter", "stick unsalted butter", "green bell pepper", "red bell pepper", "hot pepper sauce", "sweetened condensed milk", "distilled white vinegar", "squeezed lemon juice", "red pepper flakes", "extra-virgin olive oil", "rice wine vinegar", "extra virgin olive oil"];

/* handling autocomplete */
function addAutoComplete(inputFieldNum){
    var ing = document.getElementById('ingredient'+inputFieldNum);
    var thisAwesomplete = new Awesomplete(ing, {
        autoFirst: true,
        maxItems: 10,
        list: tokens
    });
}

/* handling startButton */
var startButton = document.getElementById('startButton');
startButton.onclick = function(){
    document.getElementById('ingredientsForm').style.visibility = 'visible';
    document.getElementById('mainHeaderImg').style.visibility = 'visible';
    for(var i = 1; i < 6; i++){
        addAutoComplete(i);
    }
    startButton.style.display = 'none';
};

/* handling addition of extra ingredients to the form */
var inputFieldsCounter = 6;

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

function getRelevantJson(){
    var fileToRead = "";
    // determine which file to read
    var categorieSelector = document.getElementById('categorySelect');
    var submittedCategory = categorieSelector.options[categorieSelector.selectedIndex].value;
    // alert(submittedCategory);
    switch (submittedCategory){
        case "I'm feeling spicy":
            fileToRead += JSON_ALL;
            break;
        case "Desert":
            fileToRead += JSON_DESERTS;
            break;
        case "Appetizers&Snacks":
            fileToRead += JSON_APPETIZERS;
            break;
        case "Salad":
            fileToRead += JSON_SALAD;
            break;
        case "Meat&Poultry":
            fileToRead += JSON_MEAT;
            break;
        case "Italian":
            fileToRead += JSON_ITALIAN;
            break;
        case "Easy":
            fileToRead += JSON_EASY;
            break;
        case "Soup":
            fileToRead += JSON_SOUP;
            break;
        case "Drinks":
            fileToRead += JSON_DRINKS;
            break;
        default:
            fileToRead += JSON_ALL;
            break;
    }

    // reading file
    var jsonText = readTextFile(fileToRead);
    jsonObj = JSON.parse(jsonText);
}

function handleEmptyForm(){
    document.getElementById('ingredientsForm').style.display = 'none';
    document.getElementById('resultsDiv').style.visibility = 'visible';

    // showing a message for the empty form
    var table = document.createElement('table');
    table.setAttribute('id', 'resultsTable');
    document.getElementById('resultsDiv').appendChild(table);
    var row = document.createElement('tr');
    table.appendChild(row);
    var col = document.createElement('td');
    row.appendChild(col);
    var bold = document.createElement('b');
    bold.innerHTML = 'Please give us a clue! add at least one ingredient to the search';
    col.appendChild(bold);
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
        document.getElementById('resultsDiv').removeChild(table);
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
                    ingsToAdd[y][OVERALL_INTEREST] += interest;
                    ingsToAdd[y][RECIPE_SPECIFIC_INTEREST].push(interest);
                    ingsToAdd[y][RECIPE_NAMES].push(recipeName);
                    ingsToAdd[y][RECIPE_URLS].push(recipeUrl);
                    ingsToAdd[y][RECIPE_IMGS].push(recipeImg);
                }
                else{
                    ingsToAdd[y] = [interest, [interest], [recipeName], [recipeUrl], [recipeImg]];
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
                    if(ingsToAdd.hasOwnProperty(y)){
                        ingsToAdd[y][OVERALL_INTEREST] += interest;
                        ingsToAdd[y][RECIPE_SPECIFIC_INTEREST].push(interest);
                        ingsToAdd[y][RECIPE_NAMES].push(recipeName);
                        ingsToAdd[y][RECIPE_URLS].push(recipeUrl);
                        ingsToAdd[y][RECIPE_IMGS].push(recipeImg);
                    }
                    else{
                        ingsToAdd[y] = [interest, [interest], [recipeName], [recipeUrl], [recipeImg]];
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
                        if(ingsToAdd.hasOwnProperty(y)){
                            ingsToAdd[y][OVERALL_INTEREST] += interest;
                            ingsToAdd[y][RECIPE_SPECIFIC_INTEREST].push(interest);
                            ingsToAdd[y][RECIPE_NAMES].push(recipeName);
                            ingsToAdd[y][RECIPE_URLS].push(recipeUrl);
                            ingsToAdd[y][RECIPE_IMGS].push(recipeImg);
                        }
                        else{
                            ingsToAdd[y] = [interest, [interest], [recipeName], [recipeUrl], [recipeImg]];
                        }
                    }
                }
                X.pop();
            }
            X.pop();
        }
        X.pop();
    }

    var sortedIngsToAdd = [];
    for (var ing in ingsToAdd)
        sortedIngsToAdd.push([ing, ingsToAdd[ing]])

    sortedIngsToAdd.sort(function(a, b) {
        return a[1][OVERALL_INTEREST] - b[1][OVERALL_INTEREST];
    }).reverse();

    return sortedIngsToAdd;
}

function getBestRelevantRecipe(alreadyShownRecipeUrls, ingsToAdd, currIng){
    var currDetails = ingsToAdd[currIng][1];
    var numRecipes = currDetails[RECIPE_SPECIFIC_INTEREST].length;

    var maxInterest = -1;
    var maxInterestsIndex = -1;
    var maxInterestNotShown = -1;
    var maxInterestsIndexNotShown = -1;
    // iterating over all relevant recipes to find the one with most interest that is not already shown
    for (var recipeNum = 0; recipeNum < numRecipes; recipeNum++){
        if(currDetails[RECIPE_SPECIFIC_INTEREST][recipeNum] > maxInterest){
            maxInterest = currDetails[RECIPE_SPECIFIC_INTEREST][recipeNum];
            maxInterestsIndex = recipeNum;
            if (!(alreadyShownRecipeUrls.includes(currDetails[RECIPE_URLS][recipeNum]))){
                maxInterestNotShown = currDetails[RECIPE_SPECIFIC_INTEREST][recipeNum];
                maxInterestsIndexNotShown = recipeNum;
            }
        }

    }

    // if we didn't find anything that wasn't already shown, we will return the to interest one.
    if(maxInterestsIndexNotShown === -1){
        return maxInterestsIndex;
    }
    else{
        return maxInterestsIndexNotShown;
    }
}

function addIngredientRowToResults(ingredientName, ingredient, ingsToAdd, table){
    var ingredientRow, ingredientCol, recipeSpan, recipeCol;
    var innerTable, innerRow, innerCol1, innerCol2, recipeImg, recipeUrl;
    var alreadyShownRecipeUrls = [];
    var recipeNumToShow;

    ingredientRow = document.createElement('tr');
    table.appendChild(ingredientRow);
    ingredientCol = document.createElement('td');
    ingredientRow.appendChild(ingredientCol);

    ingredientCol.innerHTML = ingredientName;

    recipeCol = document.createElement('td');
    recipeSpan = document.createElement('span');
    recipeCol.appendChild(recipeSpan);
    recipeSpan.setAttribute('class', 'popupRecipe');
    ingredientRow.appendChild(recipeCol);

    innerTable = document.createElement('table');
    recipeSpan.appendChild(innerTable);
    innerRow = document.createElement('tr');
    innerTable.appendChild(innerRow);

    // choosing most relevant recipe to display
    recipeNumToShow = getBestRelevantRecipe(alreadyShownRecipeUrls, ingsToAdd, ingredient);

    // image
    innerCol1 = document.createElement('td');
    innerRow.appendChild(innerCol1);
    recipeImg = document.createElement('img');
    recipeImg.setAttribute('class', 'recipeImage');
    if(ingsToAdd[ingredient][1][RECIPE_IMGS][recipeNumToShow] === ''){
        recipeImg.setAttribute('src', 'default-recipe.png');
    }
    else{
        recipeImg.setAttribute('src', ingsToAdd[ingredient][1][RECIPE_IMGS][recipeNumToShow]);
    }
    innerCol1.appendChild(recipeImg);

    // recipe name and url
    innerCol2 = document.createElement('td');
    recipeUrl = document.createElement('a');
    recipeUrl.setAttribute('href', ingsToAdd[ingredient][1][RECIPE_URLS][recipeNumToShow]);
    recipeUrl.innerHTML = ingsToAdd[ingredient][1][RECIPE_NAMES][recipeNumToShow];
    innerCol2.appendChild(recipeUrl);
    innerRow.appendChild(innerCol2);
}

function handleNonEmptyForm(ingredientsList){
    // getting dictionary of all possible ingredients to add
    // the value for each ingredient is the sum of interests of the association rules it appeared in
    var sortedIngsToAdd = getIngredientsToAdd(ingredientsList);

    // displaying results
    document.getElementById('ingredientsForm').style.display = 'none';
    document.getElementById('resultsDiv').style.visibility = 'visible';

    var table = document.createElement('table');
    table.setAttribute('id', 'resultsTable');
    document.getElementById('resultsDiv').appendChild(table);
    var row, col, bold;
    // if no results were found
    if (sortedIngsToAdd.length === 0){
        row = document.createElement('tr');
        table.appendChild(row);
        col = document.createElement('td');
        col.setAttribute('colspan','2');
        row.appendChild(col);

        bold = document.createElement('b');
        bold.innerHTML = 'We found nothing to add. Your recipe is probably already AWESOME!';
        col.appendChild(bold);
    }
    else{
        row = document.createElement('tr');
        table.appendChild(row);
        col = document.createElement('td');
        col.setAttribute('colspan','2');
        row.appendChild(col);
        bold = document.createElement('b');
        bold.innerHTML = 'We think it would be cool to add one (or more) of the following:';
        col.appendChild(bold);

        var numIngredientsShown = 0;
        for(var ix = 0; ix < sortedIngsToAdd.length; ix++){
            if(numIngredientsShown === NUM_INGREDIENTS_TO_DISPLAY){
                break;
            }
            addIngredientRowToResults(sortedIngsToAdd[ix][0], ix, sortedIngsToAdd, table);
            numIngredientsShown++;
        }
    }

    // button for adding extra ingredients to the results
    var showMoreRow = document.createElement('tr');
    showMoreRow.setAttribute('id', 'showMoreRow');
    table.appendChild(showMoreRow);
    var showMoreCol = document.createElement('td');
    showMoreCol.setAttribute('colspan', '2');
    showMoreRow.appendChild(showMoreCol);
    var showMoreButton = document.createElement('button');
    showMoreButton.setAttribute('id', 'showMoreButton');
    showMoreButton.innerHTML = 'Show me more...';
    showMoreButton.onclick = function () {

        var showMore = document.getElementById('showMoreRow');
        var last = document.getElementById('lastRow');
        var startShowing = numIngredientsShown;
        table.removeChild(showMore);
        table.removeChild(last);
        for(var ingredientNum = 0; ingredientNum < sortedIngsToAdd.length; ingredientNum++){
            if(ingredientNum >= startShowing && ingredientNum <= (startShowing + 1)){
                addIngredientRowToResults(sortedIngsToAdd[ingredientNum][0], ingredientNum, sortedIngsToAdd, table);
                numIngredientsShown++;
            }
        }
        table.appendChild(showMore);
        table.appendChild(last);
    };
    showMoreCol.appendChild(showMoreButton);

    // last row: back to search button
    var lastRow = document.createElement('tr');
    lastRow.setAttribute('id', 'lastRow');
    table.appendChild(lastRow);
    var buttonCol = document.createElement('td');
    buttonCol.setAttribute('colspan','2');
    lastRow.appendChild(buttonCol);
    var backToSearchButton = document.createElement('button');
    backToSearchButton.setAttribute('id', 'backToSearch');
    backToSearchButton.innerHTML = 'Back to search';
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
    getRelevantJson();

    if(submittedElems._count === 0){
        handleEmptyForm();
    }
    else{
        handleNonEmptyForm(submittedElems._validElements);
    }
}
