



// var timing_output = '[ {  "path" : "https:\/\/mail.google.com\/mail\/u\/0",    "endDate" : "2015-02-11, 1:00 PM",    "startDate" : "2015-02-11, 12:00 PM",    "application" : "Safari",    "duration" : 1528.618035137653  }]';

// alasql('SELECT projects, duration, path, application \
// FROM json("timing_output") \
// GROUP BY projects, duration, path, application \
// ORDER BY duration DESC \
// ;\
// ',[],function(res){
//               console.log(res);
//   });

// const results = alasql(['SELECT * FROM CSV("./data/monthly_avg_price.csv", {headers:true})'])
// .then(function(res){
//   console.log(res); // output depends on mydata.xls
// }).catch(function(err){
//   console.log('Does the file exist? There was an error:', err);
// });

// console.log("results = " + results);

// var data = [ {a: 1, b: 10}, {a: 2, b: 20}, {a: 1, b: 30} ];

// var res = alasql('SELECT a, SUM(b) AS b FROM ? GROUP BY a',[data]);

// console.log("resss = " + JSON.stringify(res, null, 2));

// import * as alasql from 'alasql';

// alasql.promise('SELECT Age FROM CSV("/data.csv", {headers:true, quote:"\'",separator:","})')
// .then(function(data){
//      console.log(data);
//     console.log("Gooooodoododdoododododdo");
// }).catch(function(err){
//       console.log("Erroooorororororororororo");
//     //  console.log('Error:', err);
// });

// import * as d3 from 'd3';
// var data_json = d3.csv("data/dubai_2br_monthly_avg.csv").then(function(data) {
//   console.log("from d3");
//   console.log(data); // [{"Hello": "world"}, …]
//   return data;
// });


//import { csvParse } from 'd3-dsv';
// import dataCsv from '../data/bar_chart';
//import dataCsv from '../data/bar_chart';
//
//import * as d3 from 'd3';

// var fr=new FileReader(); 
// fr.readAsText('../data/bar_chart'); 
// console.log(fr.result)

// const fs = require('fs') 
  
// fs.readFile('../data/dubai_2br_monthly_avg_csv.js', (err, data) => { 
//     if (err) throw err; 
  
//     console.log(data.toString()); 
// }) 


// d3.text("data/testnh.csv", function(r){
//   var result = "x, y, z\n" + r;  //now you have the header
//   var data = d3.csv.parse(result);
// };

//d3.text("../data/dubai_2br_monthly_avg.csv", function(text) {
//  console.log("Helloooooooo")
//  console.log(d3.csvParseRows(text));
//});
//
//const data = csvParse(dataCsv, d => {
//  d.frequency = +d.frequency;
//  // console.log(d);
//  return d;
//});

// console.log(data);

// console.log("am i logged???")
// console.log(data_json);

//export default data;

// export default data_json;

// export default [
//     { name: 'January', uv: 4000, pv: 2400, amt: 2400 },
//     { name: 'February', uv: 3000, pv: 1398, amt: 2210 },
//     { name: 'March', uv: 2000, pv: 9800, amt: 2290 },
//     { name: 'April', uv: 2780, pv: 3908, amt: 2000 },
//     { name: 'June', uv: 1890, pv: 4800, amt: 2181 },
//     { name: 'July', uv: 2390, pv: 3800, amt: 2500 },
//     { name: 'August', uv: 3490, pv: 4300, amt: 2100 },
//     { name: 'September', uv: 3490, pv: 4300, amt: 2100 },
//     { name: 'October', uv: 3490, pv: 4300, amt: 2100 },
//     { name: 'Novemeber', uv: 3490, pv: 4300, amt: 2100 },
//     { name: 'December', uv: 3490, pv: 4300, amt: 2100 },
//   ];