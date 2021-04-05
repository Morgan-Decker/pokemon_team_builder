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