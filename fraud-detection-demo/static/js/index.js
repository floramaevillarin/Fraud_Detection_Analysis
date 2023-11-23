read_json();
setTimeout(read_data, 100);

function read_json() {

   fetch(window.location.protocol + "//" + window.location.host + '/data/fields.json').then(res => res.json()).then(fields => {
        const HTMLResponse = document.getElementById("recent_div");
        
        // table
        let tblRecent = document.createElement("table");
        tblRecent.id = "recent_table";
        tblRecent.className = "table table-striped table-bordered table-sm";
        tblRecent.cellspacing = "0";
        tblRecent.width = "100%";
        HTMLResponse.appendChild(tblRecent);

        // head
        let tHead = document.createElement("thead");
        tblRecent.appendChild(tHead);

        let trHead = document.createElement("tr");
        tHead.appendChild(trHead);
        
        fields.forEach(field => {
           let thCol = document.createElement("th");
           thCol.textContent = field.label;
           trHead.appendChild(thCol);
        });
   });
 
}

function read_data() {
   
   fetch(window.location.protocol + "//" + window.location.host + '/data/data.csv').then(res => res.text()).then(content => {
        
        const HTMLResponse = document.getElementById("recent_table");
        
        // body
        let tBody = document.createElement("tbody");
        HTMLResponse.appendChild(tBody);
        
        let lines = content.split(/\n/);
        lines = lines.reverse()
        
        lines.forEach(line => {
           if (line != "") {
              let trBody = document.createElement("tr");
              tBody.appendChild(trBody);
              
              let fields = line.split(",");
              
              fields.forEach(field => {
                 let tdCol = document.createElement("td");
                 tdCol.textContent = field;
                 trBody.appendChild(tdCol);
              });
           }
        }); 
   });
   
}

function new_input() {
   window.open("newinput.html", "_self");
}
