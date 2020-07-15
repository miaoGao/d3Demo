 // javascript

var data = document.getElementById("data").getAttribute("value");
data = data.replace(/'/g, '"')
var json_obj = JSON.parse(data)
//console.log(json_obj[0])
// for (i = 0; i < json_obj.length; i++) {
//     //console.log(json_obj[i]['site'])
//     for (j = 0; j < json_obj[i]['stats'].length; j++) {
//         var temp = new Array();
//         temp = json_obj[i]['stats'][j];
//         console.log( temp[1] )
//     }
// }

var abcnews_quantity = new Array();
var abcnews_date = new Array();
for (i = 0; i < json_obj[0]['stats'].length; i++) {
    var temp = new Array();
    temp = json_obj[0]['stats'][i];
    abcnews_date.push(temp[0]);
    abcnews_quantity.push(temp[1]);
}

console.log(abcnews_quantity); // abcnews的新闻量
console.log(abcnews_date);

dataset = abcnews_quantity;
var svgWidth = 500, svgHeight = 300, barPadding = 5;
var barWidth = (svgWidth / dataset.length);


var svg = d3.select('svg')
    .attr("viewBox", [0, 0, svgWidth, svgHeight])
    .attr("width", svgWidth)
    .attr("height", svgHeight);


var x = d3.scaleBand()
    .domain([0, 1, 2, 3, 4, 5, 6].reverse())
    .range([0, svgWidth]);

var y = d3.scaleLinear()
    .domain([d3.max(dataset), 0])
    .range([0, svgHeight - 30]);

var xAxisTranslate = svgHeight - 20;

xAxis = g => g
    .call(d3.axisBottom(x).tickFormat(i => abcnews_date[i]).tickSizeOuter(0))

yAxis = g => g
    .call(d3.axisLeft(y))

var barChart = svg.selectAll("rect")
    .attr("fill", "steelblue")
    .data(dataset)
    .enter()
    .append("rect")
    .attr("y", function(d) {
        return svgHeight - d 
    })
    .attr("height", function(d) { 
        return d; 
    })
    .attr("width", barWidth - barPadding)   
    .attr("class", "bar")
    .attr("transform", function (d, i) {
        var translate = [barWidth * i + 30, -30]; 
        return "translate("+ translate +")";
    });

var text = svg.selectAll("text")
    .data(dataset)
    .enter()
    .append("text")
    .text(function(d) {
        return d;
    })
    .attr("y", function(d, i) {
        return svgHeight - d - 2;
    })
    .attr("x", function(d, i) {
        return barWidth * i;
    })
    .attr("fill", "#A64C38");


svg.append("g")
    .attr("transform", "translate(25, 30)")
    .call(yAxis);
         
var xAxisTranslate = svgHeight - 20;
         
svg.append("g")
    .attr("transform", `translate(25,${svgHeight - 30})`)
    .call(xAxis);
