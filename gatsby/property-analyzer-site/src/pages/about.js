import React from 'react'
import Layout from '../components/layout/Layout';
// import Plot from 'react-plotly.js';
import loadable from '@loadable/component';
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
          {
            x: [1, 2, 3],
            y: [2, 6, 3],
            type: 'scatter',
            mode: 'lines+markers',
            marker: {color: 'red'},
          },
          {type: 'bar', x: [1, 2, 3], y: [2, 5, 3]},
        ]}
        layout={{width: 320, height: 240, title: 'A Fancy Plot'}}
      />    
      </Layout>
    )
  }