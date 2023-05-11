function setmenu2() {
    var menu1 = document.getElementById('menu1');
    var sel   = menu1.options[menu1.selectedIndex].text;
    var menu2 = document.getElementById('menu2');

      if (sel == "Moyenne (Par défaut)") {
      menu2.innerHTML = "<option value='fa-regular fa-chart-bar'>&#xf080; Diagramme en bâtonnets</option>"
                       +"<option value='fa-solid fa-chart-line'>&#xf201; Courbe</option>";
      } else if (sel == "Minimum") {
      menu2.innerHTML = "<option value='fa-regular fa-signal'>&#xf012; Stem</option>";
      } else if (sel == "Maximum") {
      menu2.innerHTML = "<option value='fa-regular fa-signal'>&#xf012; Stem</option>";
      } else {
      menu2.innerHTML = "<option value='fa-regular fa-chart-bar'>&#xf080; Diagramme en bâtonnets</option>"
                       +"<option value='fa-solid fa-chart-line'>&#xf201; Courbe</option>"
                       +"<option value='fa-solid fa-chart-pie'>&#xf200; Secteur</option>";
      }
  }