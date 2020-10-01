import React, { useState, useEffect } from "react";
import Layout from '../components/layout/Layout';
import '../css/chart.css';
import dpprices from '../data/dubai_prop_prices'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts'

export default function Recharts_tst() {
  return (
    <Layout>
    <section className="pt-20 md:pt-40">
      <div className="container mx-auto px-8 lg:flex">
        <div className="text-center lg:text-left lg:w-1/2">    

        <LineChart
            width={400}
            height={400}
            data={dpprices}
            margin={{ top: 5, right: 20, left: 10, bottom: 5 }}
            >
            <XAxis dataKey="name" />
            <Tooltip />
            <CartesianGrid stroke="#f5f5f5" />
            <Line type="monotone" dataKey="uv" stroke="#ff7300" yAxisId={0} />
            <Line type="monotone" dataKey="pv" stroke="#387908" yAxisId={1} />
            </LineChart>

                </div>
            </div>
        </section>
        </Layout>  
  )
}

