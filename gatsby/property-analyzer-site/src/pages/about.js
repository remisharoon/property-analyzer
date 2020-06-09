import React from 'react'
import Layout from '../components/layout/Layout';
// import Plot from 'react-plotly.js';
import loadable from '@loadable/component';
import test_plot from '../data/test_plot';

const Plot = loadable(() => import('react-plotly.js'))


export default function About() {
    return (
        <Layout>
      <div style={{ color: `teal` }}>
        <h1>About Property Analyzer</h1>
        <p>Such wow. This is an awesome tool.</p>
      </div>
      <Plot
        data={[
            test_plot.high_2000, 
            test_plot.month,
          ]}
          graphDiv="graph"
      />    
      </Layout>
    )
  }