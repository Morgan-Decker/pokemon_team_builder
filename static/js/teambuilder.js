var changeSprite_1 = function () {
    document.getElementById('image1').src = "/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png"
}
var changeGigantamax_1 = function () {
    document.getElementById('gigantamax_image1').src = "/static/img/gigantamax/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changeType1_1 = function () {
    document.getElementById('type1_image1').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[2] + ".png"
}

var changeType2_1 = function () {
    document.getElementById('type2_image1').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[3] + ".png"
}

var changebutton_1 = function () {
    document.getElementById('team_image1').style.backgroundImage = "url('/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png"
}

var changemove1_1 = function () {
    document.getElementById('move1_image1').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changemove2_1 = function () {
    document.getElementById('move2_image1').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changemove3_1 = function () {
    document.getElementById('move3_image1').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changemove4_1 = function () {
    document.getElementById('move4_image1').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changeSprite_2 = function () {
    document.getElementById('image2').src = "/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png"
}
var changeGigantamax_2 = function () {
    document.getElementById('gigantamax_image2').src = "/static/img/gigantamax/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changeType1_2 = function () {
    document.getElementById('type1_image2').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[2] + ".png"
}

var changeType2_2 = function () {
    document.getElementById('type2_image2').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[3] + ".png"
}

var changebutton_2 = function () {
    document.getElementById('team_image2').style.backgroundImage = "url('/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png')"
}

var changemove1_2 = function () {
    document.getElementById('move1_image2').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changemove2_2 = function () {
    document.getElementById('move2_image2').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changemove3_2 = function () {
    document.getElementById('move3_image2').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changemove4_2 = function () {
    document.getElementById('move4_image2').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changeSprite_3 = function () {
    document.getElementById('image3').src = "/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png"
}
var changeGigantamax_3 = function () {
    document.getElementById('gigantamax_image3').src = "/static/img/gigantamax/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changeType1_3 = function () {
    document.getElementById('type1_image3').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[2] + ".png"
}

var changeType2_3 = function () {
    document.getElementById('type2_image3').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[3] + ".png"
}

var changebutton_3 = function () {
    document.getElementById('team_image3').style.backgroundImage = "url('/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png')"
}

var changemove1_3 = function () {
    document.getElementById('move1_image3').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changemove2_3 = function () {
    document.getElementById('move2_image3').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changemove3_3 = function () {
    document.getElementById('move3_image3').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var changemove4_3 = function () {
    document.getElementById('move4_image3').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

var calculateStats_1 = function () {
    var base_hp = parseInt(this.options[this.selectedIndex].value.split("|")[4])
    var base_atk = parseInt(this.options[this.selectedIndex].value.split("|")[5])
    var base_def = parseInt(this.options[this.selectedIndex].value.split("|")[6])
    var base_sp_atk = parseInt(this.options[this.selectedIndex].value.split("|")[7])
    var base_sp_def = parseInt(this.options[this.selectedIndex].value.split("|")[8])
    var base_spd = parseInt(this.options[this.selectedIndex].value.split("|")[9])
    var hpEV = parseInt(document.getElementById('hpEV1').value)
    var atkEV = parseInt(document.getElementById('atkEV1').value)
    var defEV = parseInt(document.getElementById('defEV1').value)
    var sp_atkEV = parseInt(document.getElementById('sp_atkEV1').value)
    var sp_defEV = parseInt(document.getElementById('sp_defEV1').value)
    var spdEV = parseInt(document.getElementById('spdEV1').value)
    var hpIV = parseInt(document.getElementById('hpEV1').value)
    var atkIV = parseInt(document.getElementById('atkIV1').value)
    var defIV = parseInt(document.getElementById('defIV1').value)
    var sp_atkIV = parseInt(document.getElementById('sp_atkIV1').value)
    var sp_defIV = parseInt(document.getElementById('sp_defIV1').value)
    var spdIV = parseInt(document.getElementById('spdIV1').value)
    var level = parseInt(document.getElementById('level1').value)
    var nature_upstat = document.getElementById('selectnature1').value.split("|")[1]
    var nature_downstat = document.getElementById('selectnature1').value.split("|")[2]
    var atk_nature = 1
    var def_nature = 1
    var sp_atk_nature = 1
    var sp_def_nature = 1
    var spd_nature = 1
    switch(nature_upstat) {
    case "attack":
        atk_nature = 1.1
        break;
    case "defence":
        def_nature = 1.1
        break;
    case "sp_atk":
        sp_atk_nature = 1.1
        break;
    case "sp_def":
        sp_def_nature = 1.1
        break;
    case "speed":
        spd_nature = 1.1
        break;
    default:
        break;
    }
    switch(nature_downstat) {
    case "attack":
        atk_nature = 0.9
        break;
    case "defence":
        def_nature = 0.9
        break;
    case "sp_atk":
        sp_atk_nature = 0.9
        break;
    case "sp_def":
        sp_def_nature = 0.9
        break;
    case "speed":
        spd_nature = 0.9
        break;
    default:
        break;
    }
    //stat calculations
    var hp = Math.floor(((2*base_hp+hpIV+Math.floor(hpEV/4))*level)/100)+level+10
    var atk = calculateStat(base_atk, atkIV, atkEV, level, atk_nature)
    var def = calculateStat(base_def, defIV, defEV, level, def_nature)
    var sp_atk = calculateStat(base_sp_atk, sp_atkIV, sp_atkEV, level, sp_atk_nature)
    var sp_def = calculateStat(base_sp_def, sp_defIV, sp_defEV, level, sp_def_nature)
    var spd = calculateStat(base_spd, spdIV, spdEV, level, spd_nature)

    document.getElementById('move4_image3').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
}

function calculateStat(base, IV, EV, level, nature){
    return Math.floor((Math.floor(((2*base+IV+Math.floor(EV)*level)/100))+5)*nature)
}


var selectpokemon1 = document.getElementById('selectpokemon1');
var selectmove1_1 = document.getElementById('selectmove1_1');
var selectmove2_1 = document.getElementById('selectmove2_1');
var selectmove3_1 = document.getElementById('selectmove3_1');
var selectmove4_1 = document.getElementById('selectmove4_1');
selectpokemon1.addEventListener('change', changeSprite_1, false);
selectpokemon1.addEventListener('change', changeGigantamax_1, false);
selectpokemon1.addEventListener('change', changeType1_1, false);
selectpokemon1.addEventListener('change', changeType2_1, false);
selectpokemon1.addEventListener('change', changebutton_1, false);
selectmove1_1.addEventListener('change', changemove1_1, false);
selectmove2_1.addEventListener('change', changemove2_1, false);
selectmove3_1.addEventListener('change', changemove3_1, false);
selectmove4_1.addEventListener('change', changemove4_1, false);

selectpokemon1.addEventListener('change', calculateStats_1, false);

var selectpokemon2 = document.getElementById('selectpokemon2');
var selectmove1_2 = document.getElementById('selectmove1_2');
var selectmove2_2 = document.getElementById('selectmove2_2');
var selectmove3_2 = document.getElementById('selectmove3_2');
var selectmove4_2 = document.getElementById('selectmove4_2');
selectpokemon2.addEventListener('change', changeSprite_2, false);
selectpokemon2.addEventListener('change', changeGigantamax_2, false);
selectpokemon2.addEventListener('change', changeType1_2, false);
selectpokemon2.addEventListener('change', changeType2_2, false);
selectpokemon2.addEventListener('change', changebutton_2, false);
selectmove1_2.addEventListener('change', changemove1_2, false);
selectmove2_2.addEventListener('change', changemove2_2, false);
selectmove3_2.addEventListener('change', changemove3_2, false);
selectmove4_2.addEventListener('change', changemove4_2, false);

var selectpokemon3 = document.getElementById('selectpokemon3');
var selectmove1_3 = document.getElementById('selectmove1_3');
var selectmove2_3 = document.getElementById('selectmove2_3');
var selectmove3_3 = document.getElementById('selectmove3_3');
var selectmove4_3 = document.getElementById('selectmove4_3');
selectpokemon3.addEventListener('change', changeSprite_3, false);
selectpokemon3.addEventListener('change', changeGigantamax_3, false);
selectpokemon3.addEventListener('change', changeType1_3, false);
selectpokemon3.addEventListener('change', changeType2_3, false);
selectpokemon3.addEventListener('change', changebutton_3, false);
selectmove1_3.addEventListener('change', changemove1_3, false);
selectmove2_3.addEventListener('change', changemove2_3, false);
selectmove3_3.addEventListener('change', changemove3_3, false);
selectmove4_3.addEventListener('change', changemove4_3, false);




function showdiv(Id) {
    document.getElementById(Id).style.display = 'block';
}
function hidediv(Id) {
    document.getElementById(Id).style.display = 'none';
}

function team_pokemon1(){
    showdiv('team_member_1');
    hidediv('team_member_2');
    hidediv('team_member_3');
}

function team_pokemon2(){
    hidediv('team_member_1');
    showdiv('team_member_2');
    hidediv('team_member_3');
}

function team_pokemon3(){
    hidediv('team_member_1');
    hidediv('team_member_2');
    showdiv('team_member_3');
}