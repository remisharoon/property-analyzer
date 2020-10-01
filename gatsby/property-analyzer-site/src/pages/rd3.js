// import React, { component , useState, useEffect } from 'react';
// import Layout from '../components/layout/Layout';
// // import '../css/chart.css';
// import * as d3 from 'd3';
// import node from '../components/BarChart.js';
// // import '../css/BarChart.css';

// // import node from './diagram';
// import rd3 from 'react-d3-library';
// import dataTsv from '../data/bar_chart';
// import '../css/chart.css';
// import * as D3 from "d3"
// import { useD3 } from "d3blackbox"
// import { scaleBand, scaleLinear } from 'd3-scale';
// import { tsvParse } from 'd3-dsv';
// import { max } from 'd3-array';
// import { axisBottom, axisLeft } from 'd3-axis';
// import { select } from 'd3-selection';

// const svgWidth = 560,
//   svgHeight = 300;

// //Note: getting width and height from a variable rather than the elements attribute e.g. svg.attr("width")
// const margin = { top: 20, right: 20, bottom: 30, left: 40 },
//   width = svgWidth - margin.left - margin.right,
//   height = svgHeight - margin.top - margin.bottom;

// const x = scaleBand()
//     .rangeRound([0, width])
//     .padding(0.1),
//   y = scaleLinear().rangeRound([height, 0]);

// const data = tsvParse(dataTsv, d => {
//   d.frequency = +d.frequency;
//   return d;
// });

// x.domain(data.map(d => d.letter));
// y.domain([0, max(data, d => d.frequency)]);

// export default function About() {
//     return (
//         <Layout>
//           <section className="pt-20 md:pt-40">
//             <div className="container mx-auto px-8 lg:flex">
//               <div className="text-center lg:text-left lg:w-1/2">    
//               <svg width={svgWidth} height={svgHeight}>
//           <g transform={`translate(${margin.left}, ${margin.top})`}>
//             <g
//               className="axis axis--x"
//               transform={`translate(0, ${height})`}
//               ref={node => select(node).call(axisBottom(x))}
//             />
//             <g className="axis axis--y">
//               <g ref={node => select(node).call(axisLeft(y).ticks(10, '%'))} />
//               {/* Note: In the actual example 'Frequency' is a child of the above 'g' and it doesn't render. 
//                 * Changing it to a sibiling allows it to render and having the axis as an empty 'g' means that it will also play nicer with react:
//                 * "The easiest way to avoid conflicts is to prevent the React component from updating. You can do this by rendering elements that React has no reason to update, like an empty <div />."
//                 * https://reactjs.org/docs/integrating-with-other-libraries.html 
//                 */}
//               <text transform="rotate(-90)" y="6" dy="0.71em" textAnchor="end">
//                 Frequency
//               </text>
//             </g>
//             {data.map(d => (
//               <rect
//                 key={d.letter}
//                 className="bar"
//                 x={x(d.letter)}
//                 y={y(d.frequency)}
//                 width={x.bandwidth()}
//                 height={height - y(d.frequency)}
//               />
//             ))}
//           </g>
//         </svg>
//               </div>      
//             </div>      
//           </section>

  
//       </Layout>
//     )
//   }