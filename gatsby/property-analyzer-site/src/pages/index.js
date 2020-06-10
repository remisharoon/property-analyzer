import React from 'react';
import Button from '../components/Button';
import Card from '../components/Card';
import CustomerCard from '../components/CustomerCard';
import LabelText from '../components/LabelText';
import Layout from '../components/layout/Layout';
import SplitSection from '../components/SplitSection';
import StatsBox from '../components/StatsBox';
import customerData from '../data/customer-data';
import HeroImage from '../svg/HeroImage';
import SvgCharts from '../svg/SvgCharts';
// import Plot from 'react-plotly.js';
import loadable from '@loadable/component';
import test_plot from '../data/test_plot';

import dataTsv from '../data/bar_chart';
import '../css/chart.css';
import * as D3 from "d3"
import { useD3 } from "d3blackbox"
import { scaleBand, scaleLinear } from 'd3-scale';
import { tsvParse } from 'd3-dsv';
import { max } from 'd3-array';
import { axisBottom, axisLeft } from 'd3-axis';
import { select } from 'd3-selection';

const Plot = loadable(() => import('react-plotly.js'))

const svgWidth = 560,
  svgHeight = 300;

//Note: getting width and height from a variable rather than the elements attribute e.g. svg.attr("width")
const margin = { top: 20, right: 20, bottom: 30, left: 40 },
  width = svgWidth - margin.left - margin.right,
  height = svgHeight - margin.top - margin.bottom;

const x = scaleBand()
    .rangeRound([0, width])
    .padding(0.1),
  y = scaleLinear().rangeRound([height, 0]);

const data = tsvParse(dataTsv, d => {
  d.frequency = +d.frequency;
  return d;
});

x.domain(data.map(d => d.letter));
y.domain([0, max(data, d => d.frequency)]);

export default () => (
  <Layout>
    <section className="pt-20 md:pt-40">
      <div className="container mx-auto px-8 lg:flex">
        <div className="text-center lg:text-left lg:w-1/2">
          <h1 className="text-4xl lg:text-5xl xl:text-6xl font-bold leading-none">
            Propery Analyzer
          </h1>
          <p className="text-xl lg:text-2xl mt-6 font-light">
          Analyse the housing market and research individual properties from your desk. You'll find data on prices, price/sqft, rental yields, planning, boundaries & footprints and much more.
          </p>
          <p className="mt-8 md:mt-12">
            <Button size="lg">Get Started</Button>
          </p>
          <p className="mt-4 text-gray-600">Awesome</p>
        </div>

        <Plot
          data={[
            {
              type: 'scatter',
              mode: 'lines+points',
              x: test_plot.month,
              y: test_plot.high_2007,
              marker: {color: 'red'},
              name: "2007"
            },
            {
              type: 'bar',
              x: test_plot.month,
              y: test_plot.low_2014,
              marker: {color: 'blue'},
              name: "2014"
            }
          ]}

          layout={{
            width: 720,
            height: 440,
            title: 'Housing Prices Trend'
          }}
        />

        {/* <div className="lg:w-1/2">
          <HeroImage />
        </div> */}

      <svg width={svgWidth} height={svgHeight}>
          <g transform={`translate(${margin.left}, ${margin.top})`}>
            <g
              className="axis axis--x"
              transform={`translate(0, ${height})`}
              ref={node => select(node).call(axisBottom(x))}
            />
            <g className="axis axis--y">
              <g ref={node => select(node).call(axisLeft(y).ticks(10, '%'))} />
              {/* Note: In the actual example 'Frequency' is a child of the above 'g' and it doesn't render. 
                * Changing it to a sibiling allows it to render and having the axis as an empty 'g' means that it will also play nicer with react:
                * "The easiest way to avoid conflicts is to prevent the React component from updating. You can do this by rendering elements that React has no reason to update, like an empty <div />."
                * https://reactjs.org/docs/integrating-with-other-libraries.html 
                */}
              <text transform="rotate(-90)" y="6" dy="0.71em" textAnchor="end">
                Frequency
              </text>
            </g>
            {data.map(d => (
              <rect
                key={d.letter}
                className="bar"
                x={x(d.letter)}
                y={y(d.frequency)}
                width={x.bandwidth()}
                height={height - y(d.frequency)}
              />
            ))}
          </g>
        </svg>

      </div>
    </section>
    <section id="features" className="py-20 lg:pb-40 lg:pt-48">
      <div className="container mx-auto text-center">
        <h2 className="text-3xl lg:text-5xl font-semibold">Main Features</h2>
        <div className="flex flex-col sm:flex-row sm:-mx-3 mt-12">
          <div className="flex-1 px-3">
            <Card className="mb-8">
              <p className="font-semibold text-xl">Service One</p>
              <p className="mt-4">
                An enim nullam tempor gravida donec enim ipsum blandit porta justo integer odio
                velna vitae auctor integer.
              </p>
            </Card>
          </div>
          <div className="flex-1 px-3">
            <Card className="mb-8">
              <p className="font-semibold text-xl">Service Two</p>
              <p className="mt-4">
                An enim nullam tempor gravida donec enim ipsum blandit porta justo integer odio
                velna vitae auctor integer.
              </p>
            </Card>
          </div>
          <div className="flex-1 px-3">
            <Card className="mb-8">
              <p className="font-semibold text-xl">Service Three</p>
              <p className="mt-4">
                An enim nullam tempor gravida donec enim ipsum blandit porta justo integer odio
                velna vitae auctor integer.
              </p>
            </Card>
          </div>
        </div>
      </div>
    </section>
    <SplitSection
      id="services"
      primarySlot={
        <div className="lg:pr-32 xl:pr-48">
          <h3 className="text-3xl font-semibold leading-tight">Market Analysis</h3>
          <p className="mt-8 text-xl font-light leading-relaxed">
            Our team of enthusiastic marketers will analyse and evaluate how your company stacks
            against the closest competitors
          </p>
        </div>
      }
      secondarySlot={<SvgCharts />}
    />
    <SplitSection
      reverseOrder
      primarySlot={
        <div className="lg:pl-32 xl:pl-48">
          <h3 className="text-3xl font-semibold leading-tight">
            Design And Plan Your Business Growth Steps
          </h3>
          <p className="mt-8 text-xl font-light leading-relaxed">
            Once the market analysis process is completed our staff will search for opportunities
            that are in reach
          </p>
        </div>
      }
      secondarySlot={<SvgCharts />}
    />
    <SplitSection
      primarySlot={
        <div className="lg:pr-32 xl:pr-48">
          <h3 className="text-3xl font-semibold leading-tight">
            Search For Performance Optimization
          </h3>
          <p className="mt-8 text-xl font-light leading-relaxed">
            With all the information in place you will be presented with an action plan that your
            company needs to follow
          </p>
        </div>
      }
      secondarySlot={<SvgCharts />}
    />
    <section id="stats" className="py-20 lg:pt-32">
      <div className="container mx-auto text-center">
        <LabelText className="text-gray-600">Our customers get results</LabelText>
        <div className="flex flex-col sm:flex-row mt-8 lg:px-24">
          <div className="w-full sm:w-1/3">
            <StatsBox primaryText="+100%" secondaryText="Stats Information" />
          </div>
          <div className="w-full sm:w-1/3">
            <StatsBox primaryText="+100%" secondaryText="Stats Information" />
          </div>
          <div className="w-full sm:w-1/3">
            <StatsBox primaryText="+100%" secondaryText="Stats Information" />
          </div>
        </div>
      </div>
    </section>
    <section id="testimonials" className="py-20 lg:py-40">
      <div className="container mx-auto">
        <LabelText className="mb-8 text-gray-600 text-center">What customers are saying</LabelText>
        <div className="flex flex-col md:flex-row md:-mx-3">
          {customerData.map(customer => (
            <div key={customer.customerName} className="flex-1 px-3">
              <CustomerCard customer={customer} />
            </div>
          ))}
        </div>
      </div>
    </section>
    <section className="container mx-auto my-20 py-24 bg-gray-200 rounded-lg text-center">
      <h3 className="text-5xl font-semibold">Ready to grow your business?</h3>
      <p className="mt-8 text-xl font-light">
        Quis lectus nulla at volutpat diam ut. Enim lobortis scelerisque fermentum dui faucibus in.
      </p>
      <p className="mt-8">
        <Button size="xl">Get Started Now</Button>
      </p>
    </section>
  </Layout>
);
