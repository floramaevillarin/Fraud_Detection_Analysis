read_json()

function read_json() {

   fetch('data/fields.json').then(res => res.json()).then(fields => {
         
         const HTMLResponse = document.getElementById("new_input_div");
         
         // table
         let tblInput = document.createElement("table");
         tblInput.className = "table table-striped table-bordered table-sm";
         tblInput.cellspacing = "0";
         tblInput.width = "100%";
         HTMLResponse.appendChild(tblInput);
         
         //head
         let thead = document.createElement("thead");
         tblInput.appendChild(thead);

         let trHead = document.createElement("tr");
         thead.appendChild(trHead);

         let thColFeat = document.createElement("th");
         thColFeat.textContent = "Feature";
         trHead.appendChild(thColFeat);
         
         let thColValue = document.createElement("th");
         thColValue.textContent = "Value";
         trHead.appendChild(thColValue);
         
         //body
         let tBody = document.createElement("tbody");
         tblInput.appendChild(tBody);
         
         fields.forEach(field => {
            
            let trBody = document.createElement("tr");
            tBody.appendChild(trBody);

            let tdColFeat = document.createElement("td");
            tdColFeat.textContent = field.label;
            trBody.appendChild(tdColFeat);
            
            let tdColCtrl = document.createElement("td");
            trBody.appendChild(tdColCtrl);
            
            switch (field.type) {
               case "text":
                    let textField = document.createElement("input");
                    textField.type = "text";
                    textField.required = "True";
                    textField.id = field.name;
                    textField.name = field.name;
                  //textField.className = "textField";
                    textField.className = "param";
                    tdColCtrl.appendChild(textField);
                    break;

               case "number":
                    let txtNumField = document.createElement("input");
                    txtNumField.type = "number";
                    txtNumField.required = "True";
                    txtNumField.id = field.name;
                    txtNumField.name = field.name;
                  //txtNumField.className = "numField";
                    txtNumField.className = "param numField";
                    txtNumField.min = field.min;
                    txtNumField.max = field.max;
                    txtNumField.step = field.step;
                    tdColCtrl.appendChild(txtNumField);
                    break;
                    
               case "list": 
                    let listField = document.createElement("select");
                    listField.id = field.name;
                    listField.name = field.name;
                    listField.className = "param";
                    tdColCtrl.appendChild(listField);
                    
                    for (i in field.values) {
                        let optField = document.createElement("option");
                        optField.value = field.values[i].code;
                        optField.textContent = field.values[i].value; 
                        listField.appendChild(optField);
                    }
                    
                    break;
                    
               case "radio":
                    
                    for (i in field.values) {
                        let rdField = document.createElement("input");
                        rdField.type = "radio";
                        rdField.name = field.name;
                        rdField.id = field.values[i].code;
                        rdField.value = field.values[i].code;
                        rdField.className = "param";
                      //rdField.textContent = field.values[i].value;
                        tdColCtrl.appendChild(rdField);

                        let lblField = document.createElement("label");
                        lblField.textContent = field.values[i].value;
                        tdColCtrl.appendChild(lblField);

                        tdColCtrl.appendChild(document.createElement("br"));
                    }
                    
                    break;
            }
 
       });
   });

 }

 function getPrediction()
 {
   // defining API rest URL
   const API_URL = "https://fraud-detection-demo-5b6679a4c9d0.herokuapp.com/api/prediction"

   // initializing the label result
   const lblResult = document.getElementById("lblResult");
   lblResult.textContent = "PREDICTING...";

   // reading input params
   const paramList = document.getElementsByClassName("param");
   let params = {};
   
   for (i in paramList) {
       switch (paramList[i].type) {
          case "text":
               console.log(paramList[i].name + " : ", paramList[i].value);
               params[paramList[i].name] = paramList[i].value;
               break;
          case "number":
               console.log(paramList[i].name + " : ", paramList[i].value);
               params[paramList[i].name] = paramList[i].value;
               break;
          case "select-one":
               console.log(paramList[i].name + " : ", paramList[i].value);
               params[paramList[i].name] = paramList[i].value;
               break;
          case "radio":
               if (paramList[i].checked) {
                  console.log(paramList[i].name + " : ", paramList[i].value);
                  params[paramList[i].name] = paramList[i].value;
               }
               break;
       }
   };
   
   // making up the API request
   let requestHead = new Headers();
   requestHead.append("Content-Type", "application/json");
   
   /*
   let param = {};
   param.param01 = "1";
   param.param02 = "2";
   param.param03 = "3";
   param.param04 = "4";
   param.param05 = "5";
   */
   
   let requestOpt = {}; 
   requestOpt.method = "POST"
   requestOpt.body = JSON.stringify(params);
   requestOpt.headers = requestHead;
   
   fetch(`${API_URL}`, requestOpt).then(res => res.json()).catch(error => console.error('Error:', error)).then(response => {
        const result = response.result;
        lblResult.textContent = "Prediction: " + result;
   });

 }
