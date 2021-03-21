import React, { useState, useEffect } from "react"
import Layout from '../components/layout/Layout';
import LabelText from '../components/LabelText';
import CustomerCard from '../components/CustomerCard';
import '../css/chart.css';

export default function Knowledge() {
    return (
        <Layout>
          <section className="pt-20 md:pt-40">
            <div className="container mx-auto px-8 lg:flex">
              <div className="text-center lg:text-left lg:w-1/2">    
                <h3>PA Knowledge Center</h3>

                <p>Such wow. This is an awesome place to learn new stuff about property markets.</p>

                
              </div>      
            </div>      
          </section>

          <section id="testimonials" className="py-20 lg:py-40">
            <div className="container mx-auto">
                <LabelText className="mb-6 text-gray-600 text-left">A guide to buying property in dubai</LabelText>
                <div className="flex flex-col md:flex-row md:-mx-3">
                    <p>
                    <ul>
                    <li>Deposits as per Agreement of sale between Buyer & Seller</li>
                    <li>Transfer fees with the Land Department</li>
                    <li>Connection fees for electricity and water authorities</li>
                    <li>Community service fees</li>
                    <li>Mortgage application fees if required</li>
                    <li>Misc admin fees to the Land Department</li>
                    <li>Commission</li>

                    </ul>                          
                    </p>
                  
                </div>
            </div>
          </section>
  
      </Layout>
    )
  }