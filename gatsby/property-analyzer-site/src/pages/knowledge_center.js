import React, { useState, useEffect } from "react"
import Layout from '../components/layout/Layout';
import LabelText from '../components/LabelText';
import CustomerCard from '../components/CustomerCard';
// import Article from "../components/Article/";
// import {Row, Col,} from 'antd';
import SplitSection from '../components/SplitSection';
import SvgCharts from '../svg/SvgCharts';

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



          <div className="container mx-auto">
              <div className="text-center lg:text-left lg:w-1/2">    
                <button className="bg-green-600">Button</button>
              </div>      
          </div>      

        <div className="container mx-auto px-16 items-center flex flex-col lg:flex-row">
          <div className="lg:w-1/2">
            <div className="lg:pl-32 xl:pl-48">
                <h3 className="text-3xl font-semibold leading-tight">
                  Design And Plan Your Business Growth Steps
                </h3>
                <p className="mt-8 text-xl font-light leading-relaxed">
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
        </div>          


        <div class="p-10">  
        <div class="max-w-sm rounded overflow-hidden shadow-lg">
          {/* <img class="w-full" src="/mountain.jpg" alt="Mountain"> */}
          <div class="px-6 py-4">
              <div class="font-bold text-xl mb-2">Mountain</div>
              <p class="text-gray-700 text-base">
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus quia, nulla! Maiores et perferendis eaque, exercitationem praesentium nihil.
              </p>
              </div>
            <div class="px-6 pt-4 pb-2">
              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#photography</span>
              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#travel</span>
              <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#winter</span>
            </div>
          </div>
        </div>
        

      <div class="w-full sm:w-1/2 md:w-1/3">
        <h1 class="font-sans font-thin mb-4">Article title</h1>

        <p class="text-grey mb-3">Written by Walter Bishop on 25 May 2070. Posted in News</p>

        <h2 class="font-sans font-thin leading-normal mb-4">The observers are coming. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi.</h2>

        <p class="text-grey-darkest mb-6 leading-tight">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

        <div>
          <a href="#" class="text-black mr-2">READ MORE</a>
          <a href="#" class="text-black">5 COMMENTS</a>
        </div>

      </div>

          <section id="testimonials" className="py-20 lg:py-40">
            <div className="container mx-auto">
                <LabelText className="mb-6 text-gray-600 text-left">A guide to buying property in dubai</LabelText>
                <div className="flex flex-col md:flex-row md:-mx-3">
                    <ul>
                    <li>Deposits as per Agreement of sale between Buyer & Seller</li>
                    <li>Transfer fees with the Land Department</li>
                    <li>Connection fees for electricity and water authorities</li>
                    <li>Community service fees</li>
                    <li>Mortgage application fees if required</li>
                    <li>Misc admin fees to the Land Department</li>
                    <li>Commission</li>

                    </ul>                          
                  
                </div>
            </div>
          </section>
  

      </Layout>
    )
  }