import React, { useState, useEffect } from "react"
import Layout from '../components/layout/Layout';
import '../css/chart.css';
import {NVD3Chart} from 'react-nvd3'



export default function Nvd3() {

    var TestData = [{
        key: "Cumulative Return",
        values: [
            {
                "label" : "A" ,
                "value" : -29.765957771107
            } ,
            {
                "label" : "B" ,
                "value" : 0
            } ,
            {
                "label" : "C" ,
                "value" : 32.807804682612
            } ,
            {
                "label" : "D" ,
                "value" : 196.45946739256
            } ,
            {
                "label" : "E" ,
                "value" : 0.19434030906893
            } ,
            {
                "label" : "F" ,
                "value" : -98.079782601442
            } ,
            {
                "label" : "G" ,
                "value" : -13.925743130903
            } ,
            {
                "label" : "H" ,
                "value" : -5.1387322875705
            }
        ]
    }];    

    return (
        <Layout>
          <section className="pt-20 md:pt-40">
            <div className="container mx-auto px-8 lg:flex">
              <div className="text-center lg:text-left lg:w-1/2">    

                <NVD3Chart id="chart" type="discreteBarChart" datum={TestData} x="label" y="value"/>
                ,
                    document.getElementById('barChart')

              </div>      
            </div>      
          </section>

  
      </Layout>
    )
  }