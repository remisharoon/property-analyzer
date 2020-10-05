import * as alasql from 'alasql';

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

alasql.promise('SELECT col1 FROM CSV("monthly_avg_price.csv", {headers:false, quote:"\'",separator:","})')
.then(function(data){
     console.log(data);
    console.log("Gooooodoododdoododododdo");
}).catch(function(err){
      console.log("Erroooorororororororororo");
    //  console.log('Error:', err);
});

export default [
    { name: 'January', uv: 4000, pv: 2400, amt: 2400 },
    { name: 'February', uv: 3000, pv: 1398, amt: 2210 },
    { name: 'March', uv: 2000, pv: 9800, amt: 2290 },
    { name: 'April', uv: 2780, pv: 3908, amt: 2000 },
    { name: 'June', uv: 1890, pv: 4800, amt: 2181 },
    { name: 'July', uv: 2390, pv: 3800, amt: 2500 },
    { name: 'August', uv: 3490, pv: 4300, amt: 2100 },
    { name: 'September', uv: 3490, pv: 4300, amt: 2100 },
    { name: 'October', uv: 3490, pv: 4300, amt: 2100 },
    { name: 'Novemeber', uv: 3490, pv: 4300, amt: 2100 },
    { name: 'December', uv: 3490, pv: 4300, amt: 2100 },
  ];