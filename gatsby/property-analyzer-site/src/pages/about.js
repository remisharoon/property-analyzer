import React, { useState, useEffect } from "react"
import Layout from '../components/layout/Layout';
import '../css/chart.css';


// export default function About() {
//   return (
//     <Layout>
//     <section className="pt-20 md:pt-40">
//       <div className="container mx-auto px-8 lg:flex">
//         <div className="text-center lg:text-left lg:w-1/2">    
//   </div>
//   </div>
//   </section>
//   </Layout>  
//   )
// }

export default function About() {
    return (
        <Layout>
          <section className="pt-20 md:pt-40">
            <div className="container mx-auto px-8 lg:flex">
              <div className="text-center lg:text-left lg:w-1/2">    
                <h1>About Property Analyzer</h1>
                <p>Such wow. This is an awesome tool.</p>
              </div>      
            </div>      
          </section>

  
      </Layout>
    )
  }