//------------------------------------------------Element Changers----------------------------------------------------------------
var changeSprite_1 = function () {
    document.getElementById('image1').src = "/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png"
    document.getElementById('submitname1').value = this.options[this.selectedIndex].value.split("|")[10]
    document.getElementById('submitpokedex1').value = this.options[this.selectedIndex].value.split("|")[0]
}

var changeGigantamax_1 = function () {
    document.getElementById('gigantamax_image1').src = "/static/img/gigantamax/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById('gmaxsubmit1').value = this.options[this.selectedIndex].value.split("|")[1]
}

var changeType1_1 = function () {
    document.getElementById('type1_image1').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[2] + ".png"
    document.getElementById('type1_1').value = this.options[this.selectedIndex].value.split("|")[2]
}

var changeType2_1 = function () {
    document.getElementById('type2_image1').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[3] + ".png"
    document.getElementById('type2_1').value = this.options[this.selectedIndex].value.split("|")[3]
}

var changebutton_1 = function () {
    document.getElementById('team_image1').style.backgroundImage = "url('/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png"
}

var changemove1_1 = function () {
    document.getElementById('move1_image1').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove1_1").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype1_1").value = this.options[this.selectedIndex].value.split("|")[1]

}

var changemove2_1 = function () {
    document.getElementById('move2_image1').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove2_1").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype2_1").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove3_1 = function () {
    document.getElementById('move3_image1').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove3_1").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype3_1").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove4_1 = function () {
    document.getElementById('move4_image1').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove4_1").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype4_1").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changeSprite_2 = function () {
    document.getElementById('image2').src = "/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png"
    document.getElementById('submitname2').value = this.options[this.selectedIndex].value.split("|")[10]
    document.getElementById('submitpokedex2').value = this.options[this.selectedIndex].value.split("|")[0]
}
var changeGigantamax_2 = function () {
    document.getElementById('gigantamax_image2').src = "/static/img/gigantamax/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById('gmaxsubmit2').value = this.options[this.selectedIndex].value.split("|")[1]
}

var changeType1_2 = function () {
    document.getElementById('type1_image2').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[2] + ".png"
    document.getElementById('type1_2').value = this.options[this.selectedIndex].value.split("|")[2]
}

var changeType2_2 = function () {
    document.getElementById('type2_image2').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[3] + ".png"
    document.getElementById('type2_2').value = this.options[this.selectedIndex].value.split("|")[3]
}

var changebutton_2 = function () {
    document.getElementById('team_image2').style.backgroundImage = "url('/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png')"
}

var changemove1_2 = function () {
    document.getElementById('move1_image2').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove1_2").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype1_2").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove2_2 = function () {
    document.getElementById('move2_image2').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove2_2").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype2_2").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove3_2 = function () {
    document.getElementById('move3_image2').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove3_2").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype3_2").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove4_2 = function () {
    document.getElementById('move4_image2').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove4_2").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype4_2").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changeSprite_3 = function () {
    document.getElementById('image3').src = "/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png"
    document.getElementById('submitname3').value = this.options[this.selectedIndex].value.split("|")[10]
    document.getElementById('submitpokedex3').value = this.options[this.selectedIndex].value.split("|")[0]
}
var changeGigantamax_3 = function () {
    document.getElementById('gigantamax_image3').src = "/static/img/gigantamax/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById('gmaxsubmit3').value = this.options[this.selectedIndex].value.split("|")[1]
}

var changeType1_3 = function () {
    document.getElementById('type1_image3').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[2] + ".png"
    document.getElementById('type1_3').value = this.options[this.selectedIndex].value.split("|")[2]
}

var changeType2_3 = function () {
    document.getElementById('type2_image3').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[3] + ".png"
    document.getElementById('type2_3').value = this.options[this.selectedIndex].value.split("|")[3]
}

var changebutton_3 = function () {
    document.getElementById('team_image3').style.backgroundImage = "url('/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png')"
}

var changemove1_3 = function () {
    document.getElementById('move1_image3').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove1_3").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype1_3").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove2_3 = function () {
    document.getElementById('move2_image3').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove2_3").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype2_3").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove3_3 = function () {
    document.getElementById('move3_image3').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove3_3").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype3_3").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove4_3 = function () {
    document.getElementById('move4_image3').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove4_3").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype4_3").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changeSprite_4 = function () {
    document.getElementById('image4').src = "/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png"
    document.getElementById('submitname4').value = this.options[this.selectedIndex].value.split("|")[10]
    document.getElementById('submitpokedex4').value = this.options[this.selectedIndex].value.split("|")[0]
}
var changeGigantamax_4 = function () {
    document.getElementById('gigantamax_image4').src = "/static/img/gigantamax/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById('gmaxsubmit4').value = this.options[this.selectedIndex].value.split("|")[1]
}

var changeType1_4 = function () {
    document.getElementById('type1_image4').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[2] + ".png"
    document.getElementById('type1_4').value = this.options[this.selectedIndex].value.split("|")[2]
}

var changeType2_4 = function () {
    document.getElementById('type2_image4').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[3] + ".png"
    document.getElementById('type2_4').value = this.options[this.selectedIndex].value.split("|")[3]
}

var changebutton_4 = function () {
    document.getElementById('team_image4').style.backgroundImage = "url('/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png')"
}

var changemove1_4 = function () {
    document.getElementById('move1_image4').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove1_4").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype1_4").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove2_4 = function () {
    document.getElementById('move2_image4').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove2_4").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype2_4").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove3_4 = function () {
    document.getElementById('move3_image4').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove3_4").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype3_4").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove4_4 = function () {
    document.getElementById('move4_image4').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove4_4").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype4_4").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changeSprite_5 = function () {
    document.getElementById('image5').src = "/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png"
    document.getElementById('submitname5').value = this.options[this.selectedIndex].value.split("|")[10]
    document.getElementById('submitpokedex5').value = this.options[this.selectedIndex].value.split("|")[0]
}
var changeGigantamax_5 = function () {
    document.getElementById('gigantamax_image5').src = "/static/img/gigantamax/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById('gmaxsubmit5').value = this.options[this.selectedIndex].value.split("|")[1]
}

var changeType1_5 = function () {
    document.getElementById('type1_image5').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[2] + ".png"
    document.getElementById('type1_5').value = this.options[this.selectedIndex].value.split("|")[2]
}

var changeType2_5 = function () {
    document.getElementById('type2_image5').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[3] + ".png"
    document.getElementById('type2_5').value = this.options[this.selectedIndex].value.split("|")[3]
}

var changebutton_5 = function () {
    document.getElementById('team_image5').style.backgroundImage = "url('/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png')"
}

var changemove1_5 = function () {
    document.getElementById('move1_image5').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove1_5").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype1_5").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove2_5 = function () {
    document.getElementById('move2_image5').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove2_5").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype2_5").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove3_5 = function () {
    document.getElementById('move3_image5').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove3_5").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype3_5").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove4_5 = function () {
    document.getElementById('move4_image5').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove4_5").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype4_5").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changeSprite_6 = function () {
    document.getElementById('image6').src = "/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png"
    document.getElementById('submitname6').value = this.options[this.selectedIndex].value.split("|")[10]
    document.getElementById('submitpokedex6').value = this.options[this.selectedIndex].value.split("|")[0]
}
var changeGigantamax_6 = function () {
    document.getElementById('gigantamax_image6').src = "/static/img/gigantamax/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById('gmaxsubmit6').value = this.options[this.selectedIndex].value.split("|")[1]
}

var changeType1_6 = function () {
    document.getElementById('type1_image6').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[2] + ".png"
    document.getElementById('type1_6').value = this.options[this.selectedIndex].value.split("|")[2]
}

var changeType2_6 = function () {
    document.getElementById('type2_image6').src = "/static/img/typelogo/" +
        this.options[this.selectedIndex].value.split("|")[3] + ".png"
    document.getElementById('type2_6').value = this.options[this.selectedIndex].value.split("|")[3]
}

var changebutton_6 = function () {
    document.getElementById('team_image6').style.backgroundImage = "url('/static/img/sprites/" +
        this.options[this.selectedIndex].value.split("|")[0] + ".png')"
}

var changemove1_6 = function () {
    document.getElementById('move1_image6').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove1_6").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype1_6").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove2_6 = function () {
    document.getElementById('move2_image6').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove2_6").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype2_6").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove3_6 = function () {
    document.getElementById('move3_image6').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove3_6").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype3_6").value = this.options[this.selectedIndex].value.split("|")[1]
}

var changemove4_6 = function () {
    document.getElementById('move4_image6').src = "/static/img/types/" +
        this.options[this.selectedIndex].value.split("|")[1] + ".png"
    document.getElementById("submitmove4_6").value = this.options[this.selectedIndex].value.split("|")[0]
    document.getElementById("movetype4_6").value = this.options[this.selectedIndex].value.split("|")[1]
}

//------------------------------------------------Stat Calculations----------------------------------------------------------------

var calculateStats_1 = function () {
    calculatestats("1")
}

var calculateStats_2 = function () {
    calculatestats("2")
}

var calculateStats_3 = function () {
    calculatestats("3")
}

var calculateStats_4 = function () {
    calculatestats("4")
}

var calculateStats_5 = function () {
    calculatestats("5")
}
var calculateStats_6 = function () {
    calculatestats("6")
}

function calculatestats(i){
    var base_hp = parseInt(document.getElementById('selectpokemon'+i).value.split("|")[4])
    var base_atk = parseInt(document.getElementById('selectpokemon'+i).value.split("|")[5])
    var base_def = parseInt(document.getElementById('selectpokemon'+i).value.split("|")[6])
    var base_sp_atk = parseInt(document.getElementById('selectpokemon'+i).value.split("|")[7])
    var base_sp_def = parseInt(document.getElementById('selectpokemon'+i).value.split("|")[8])
    var base_spd = parseInt(document.getElementById('selectpokemon'+i).value.split("|")[9])
    var hpEV = parseInt(document.getElementById('hpEV'+i).value)
    var atkEV = parseInt(document.getElementById('atkEV'+i).value)
    var defEV = parseInt(document.getElementById('defEV'+i).value)
    var sp_atkEV = parseInt(document.getElementById('sp_atkEV'+i).value)
    var sp_defEV = parseInt(document.getElementById('sp_defEV'+i).value)
    var spdEV = parseInt(document.getElementById('spdEV'+i).value)
    var hpIV = parseInt(document.getElementById('hpIV'+i).value)
    var atkIV = parseInt(document.getElementById('atkIV'+i).value)
    var defIV = parseInt(document.getElementById('defIV'+i).value)
    var sp_atkIV = parseInt(document.getElementById('sp_atkIV'+i).value)
    var sp_defIV = parseInt(document.getElementById('sp_defIV'+i).value)
    var spdIV = parseInt(document.getElementById('spdIV'+i).value)
    var level = parseInt(document.getElementById('level'+i).value)
    var nature_upstat = document.getElementById('selectnature'+i).value.split("|")[1]
    var nature_downstat = document.getElementById('selectnature'+i).value.split("|")[2]
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
    var hp =( Math.floor(((2 * base_hp + hpIV + Math.floor(0.25 * hpEV)) * level)/100) + level + 10).toString()
    var atk = calculateStat(base_atk, atkIV, atkEV, level, atk_nature).toString()
    var def = calculateStat(base_def, defIV, defEV, level, def_nature).toString()
    var sp_atk = calculateStat(base_sp_atk, sp_atkIV, sp_atkEV, level, sp_atk_nature).toString()
    var sp_def = calculateStat(base_sp_def, sp_defIV, sp_defEV, level, sp_def_nature).toString()
    var spd = calculateStat(base_spd, spdIV, spdEV, level, spd_nature).toString()

    document.getElementById('hp'+i).innerHTML = hp;
    document.getElementById('atk'+i).innerHTML = atk;
    document.getElementById('def'+i).innerHTML = def;
    document.getElementById('sp_atk'+i).innerHTML = sp_atk;
    document.getElementById('sp_def'+i).innerHTML = sp_def;
    document.getElementById('spd'+i).innerHTML = spd;

    document.getElementById('hpsubmit'+i).value = hp;
    document.getElementById('atksubmit'+i).value = atk;
    document.getElementById('defsubmit'+i).value = def;
    document.getElementById('sp_atksubmit'+i).value = sp_atk;
    document.getElementById('sp_defsubmit'+i).value = sp_def;
    document.getElementById('spdsubmit'+i).value = spd;

    document.getElementById('submitnature'+i).value = document.getElementById('selectnature'+i).value.split("|")[0]
}

function calculateStat(base, IV, EV, level, nature){
    return Math.floor((Math.floor(0.01 * (2 * base + IV + Math.floor(0.25 * EV)) * level) + 5) * nature)
}

//------------------------------------------------Event Listeners----------------------------------------------------------------
//pokemon 1 -------------------------------------------------------------------
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
document.getElementById('selectnature1').addEventListener('change', calculateStats_1, false);
document.getElementById('level1').addEventListener('change', calculateStats_1, false);
document.getElementById('hpEV1').addEventListener('change', calculateStats_1, false);
document.getElementById('atkEV1').addEventListener('change', calculateStats_1, false);
document.getElementById('sp_atkEV1').addEventListener('change', calculateStats_1, false);
document.getElementById('defEV1').addEventListener('change', calculateStats_1, false);
document.getElementById('sp_defEV1').addEventListener('change', calculateStats_1, false);
document.getElementById('spdEV1').addEventListener('change', calculateStats_1, false);
document.getElementById('hpIV1').addEventListener('change', calculateStats_1, false);
document.getElementById('atkIV1').addEventListener('change', calculateStats_1, false);
document.getElementById('sp_atkIV1').addEventListener('change', calculateStats_1, false);
document.getElementById('sp_defIV1').addEventListener('change', calculateStats_1, false);
document.getElementById('defIV1').addEventListener('change', calculateStats_1, false);
document.getElementById('spdIV1').addEventListener('change', calculateStats_1, false);

//pokemon 2 -------------------------------------------------------------------
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

selectpokemon2.addEventListener('change', calculateStats_2, false);
document.getElementById('selectnature2').addEventListener('change', calculateStats_2, false);
document.getElementById('level2').addEventListener('change', calculateStats_2, false);
document.getElementById('hpEV2').addEventListener('change', calculateStats_2, false);
document.getElementById('atkEV2').addEventListener('change', calculateStats_2, false);
document.getElementById('sp_atkEV2').addEventListener('change', calculateStats_2, false);
document.getElementById('defEV2').addEventListener('change', calculateStats_2, false);
document.getElementById('sp_defEV2').addEventListener('change', calculateStats_2, false);
document.getElementById('spdEV2').addEventListener('change', calculateStats_2, false);
document.getElementById('hpIV2').addEventListener('change', calculateStats_2, false);
document.getElementById('atkIV2').addEventListener('change', calculateStats_2, false);
document.getElementById('sp_atkIV2').addEventListener('change', calculateStats_2, false);
document.getElementById('sp_defIV2').addEventListener('change', calculateStats_2, false);
document.getElementById('defIV2').addEventListener('change', calculateStats_2, false);
document.getElementById('spdIV2').addEventListener('change', calculateStats_2, false);

//pokemon 3 -------------------------------------------------------------------
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

selectpokemon3.addEventListener('change', calculateStats_3, false);
document.getElementById('selectnature3').addEventListener('change', calculateStats_3, false);
document.getElementById('level3').addEventListener('change', calculateStats_3, false);
document.getElementById('hpEV3').addEventListener('change', calculateStats_3, false);
document.getElementById('atkEV3').addEventListener('change', calculateStats_3, false);
document.getElementById('sp_atkEV3').addEventListener('change', calculateStats_3, false);
document.getElementById('defEV3').addEventListener('change', calculateStats_3, false);
document.getElementById('sp_defEV3').addEventListener('change', calculateStats_3, false);
document.getElementById('spdEV3').addEventListener('change', calculateStats_3, false);
document.getElementById('hpIV3').addEventListener('change', calculateStats_3, false);
document.getElementById('atkIV3').addEventListener('change', calculateStats_3, false);
document.getElementById('sp_atkIV3').addEventListener('change', calculateStats_3, false);
document.getElementById('sp_defIV3').addEventListener('change', calculateStats_3, false);
document.getElementById('defIV3').addEventListener('change', calculateStats_3, false);
document.getElementById('spdIV3').addEventListener('change', calculateStats_3, false);

//pokemon 4 -------------------------------------------------------------------
var selectpokemon4 = document.getElementById('selectpokemon4');
var selectmove1_4 = document.getElementById('selectmove1_4');
var selectmove2_4 = document.getElementById('selectmove2_4');
var selectmove3_4 = document.getElementById('selectmove3_4');
var selectmove4_4 = document.getElementById('selectmove4_4');
selectpokemon4.addEventListener('change', changeSprite_4, false);
selectpokemon4.addEventListener('change', changeGigantamax_4, false);
selectpokemon4.addEventListener('change', changeType1_4, false);
selectpokemon4.addEventListener('change', changeType2_4, false);
selectpokemon4.addEventListener('change', changebutton_4, false);
selectmove1_4.addEventListener('change', changemove1_4, false);
selectmove2_4.addEventListener('change', changemove2_4, false);
selectmove3_4.addEventListener('change', changemove3_4, false);
selectmove4_4.addEventListener('change', changemove4_4, false);

selectpokemon4.addEventListener('change', calculateStats_4, false);
document.getElementById('selectnature4').addEventListener('change', calculateStats_4, false);
document.getElementById('level4').addEventListener('change', calculateStats_4, false);
document.getElementById('hpEV4').addEventListener('change', calculateStats_4, false);
document.getElementById('atkEV4').addEventListener('change', calculateStats_4, false);
document.getElementById('sp_atkEV4').addEventListener('change', calculateStats_4, false);
document.getElementById('defEV4').addEventListener('change', calculateStats_4, false);
document.getElementById('sp_defEV4').addEventListener('change', calculateStats_4, false);
document.getElementById('spdEV4').addEventListener('change', calculateStats_4, false);
document.getElementById('hpIV4').addEventListener('change', calculateStats_4, false);
document.getElementById('atkIV4').addEventListener('change', calculateStats_4, false);
document.getElementById('sp_atkIV4').addEventListener('change', calculateStats_4, false);
document.getElementById('sp_defIV4').addEventListener('change', calculateStats_4, false);
document.getElementById('defIV4').addEventListener('change', calculateStats_4, false);
document.getElementById('spdIV4').addEventListener('change', calculateStats_4, false);

//pokemon 5 -------------------------------------------------------------------
var selectpokemon5 = document.getElementById('selectpokemon5');
var selectmove1_5 = document.getElementById('selectmove1_5');
var selectmove2_5 = document.getElementById('selectmove2_5');
var selectmove3_5 = document.getElementById('selectmove3_5');
var selectmove4_5 = document.getElementById('selectmove4_5');
selectpokemon5.addEventListener('change', changeSprite_5, false);
selectpokemon5.addEventListener('change', changeGigantamax_5, false);
selectpokemon5.addEventListener('change', changeType1_5, false);
selectpokemon5.addEventListener('change', changeType2_5, false);
selectpokemon5.addEventListener('change', changebutton_5, false);
selectmove1_5.addEventListener('change', changemove1_5, false);
selectmove2_5.addEventListener('change', changemove2_5, false);
selectmove3_5.addEventListener('change', changemove3_5, false);
selectmove4_5.addEventListener('change', changemove4_5, false);

selectpokemon5.addEventListener('change', calculateStats_5, false);
document.getElementById('selectnature5').addEventListener('change', calculateStats_5, false);
document.getElementById('level5').addEventListener('change', calculateStats_5, false);
document.getElementById('hpEV5').addEventListener('change', calculateStats_5, false);
document.getElementById('atkEV5').addEventListener('change', calculateStats_5, false);
document.getElementById('sp_atkEV5').addEventListener('change', calculateStats_5, false);
document.getElementById('defEV5').addEventListener('change', calculateStats_5, false);
document.getElementById('sp_defEV5').addEventListener('change', calculateStats_5, false);
document.getElementById('spdEV5').addEventListener('change', calculateStats_5, false);
document.getElementById('hpIV5').addEventListener('change', calculateStats_5, false);
document.getElementById('atkIV5').addEventListener('change', calculateStats_5, false);
document.getElementById('sp_atkIV5').addEventListener('change', calculateStats_5, false);
document.getElementById('sp_defIV5').addEventListener('change', calculateStats_5, false);
document.getElementById('defIV5').addEventListener('change', calculateStats_5, false);
document.getElementById('spdIV5').addEventListener('change', calculateStats_5, false);

//pokemon 6 -------------------------------------------------------------------
var selectpokemon6 = document.getElementById('selectpokemon6');
var selectmove1_6 = document.getElementById('selectmove1_6');
var selectmove2_6 = document.getElementById('selectmove2_6');
var selectmove3_6 = document.getElementById('selectmove3_6');
var selectmove4_6 = document.getElementById('selectmove4_6');
selectpokemon6.addEventListener('change', changeSprite_6, false);
selectpokemon6.addEventListener('change', changeGigantamax_6, false);
selectpokemon6.addEventListener('change', changeType1_6, false);
selectpokemon6.addEventListener('change', changeType2_6, false);
selectpokemon6.addEventListener('change', changebutton_6, false);
selectmove1_6.addEventListener('change', changemove1_6, false);
selectmove2_6.addEventListener('change', changemove2_6, false);
selectmove3_6.addEventListener('change', changemove3_6, false);
selectmove4_6.addEventListener('change', changemove4_6, false);

selectpokemon6.addEventListener('change', calculateStats_6, false);
document.getElementById('selectnature6').addEventListener('change', calculateStats_6, false);
document.getElementById('level6').addEventListener('change', calculateStats_6, false);
document.getElementById('hpEV6').addEventListener('change', calculateStats_6, false);
document.getElementById('atkEV6').addEventListener('change', calculateStats_6, false);
document.getElementById('sp_atkEV6').addEventListener('change', calculateStats_6, false);
document.getElementById('defEV6').addEventListener('change', calculateStats_6, false);
document.getElementById('sp_defEV6').addEventListener('change', calculateStats_6, false);
document.getElementById('spdEV6').addEventListener('change', calculateStats_6, false);
document.getElementById('hpIV6').addEventListener('change', calculateStats_6, false);
document.getElementById('atkIV6').addEventListener('change', calculateStats_6, false);
document.getElementById('sp_atkIV6').addEventListener('change', calculateStats_6, false);
document.getElementById('sp_defIV6').addEventListener('change', calculateStats_6, false);
document.getElementById('defIV6').addEventListener('change', calculateStats_6, false);
document.getElementById('spdIV6').addEventListener('change', calculateStats_6, false);


//------------------------------------------------Team Member Selection----------------------------------------------------------------

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
    hidediv('team_member_4');
    hidediv('team_member_5');
    hidediv('team_member_6');
}

function team_pokemon2(){
    hidediv('team_member_1');
    showdiv('team_member_2');
    hidediv('team_member_3');
    hidediv('team_member_4');
    hidediv('team_member_5');
    hidediv('team_member_6');
}

function team_pokemon3(){
    hidediv('team_member_1');
    hidediv('team_member_2');
    showdiv('team_member_3');
    hidediv('team_member_4');
    hidediv('team_member_5');
    hidediv('team_member_6');
}

function team_pokemon4(){
    hidediv('team_member_1');
    hidediv('team_member_2');
    hidediv('team_member_3');
    showdiv('team_member_4');
    hidediv('team_member_5');
    hidediv('team_member_6');
}

function team_pokemon5(){
    hidediv('team_member_1');
    hidediv('team_member_2');
    hidediv('team_member_3');
    hidediv('team_member_4');
    showdiv('team_member_5');
    hidediv('team_member_6');
}

function team_pokemon6(){
    hidediv('team_member_1');
    hidediv('team_member_2');
    hidediv('team_member_3');
    hidediv('team_member_4');
    hidediv('team_member_5');
    showdiv('team_member_6');
}