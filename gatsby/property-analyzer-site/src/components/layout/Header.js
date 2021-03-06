import React from 'react';
// import { NavLink, BrowserRouter, Link} from "react-router-dom";
import { Link } from "gatsby"
import AnchorLink from 'react-anchor-link-smooth-scroll';
import LogoIcon from '../../svg/LogoIcon';
import Button from '../Button';

const Header = () => (
  <header className="sticky top-0 bg-white shadow">
    <div className="container flex flex-col sm:flex-row justify-between items-center mx-auto py-4 px-8">
      <div className="flex items-center text-2xl">
        <div className="w-12 mr-3">
          <LogoIcon />
        </div>
        
      </div>
      <div className="flex mt-4 sm:mt-0">
        <AnchorLink className="px-4" href="#features">
          Features
        </AnchorLink>
        <AnchorLink className="px-4" href="#services">
          Services
        </AnchorLink>
        <AnchorLink className="px-3" href="#stats">
          Stats
        </AnchorLink>
        <AnchorLink className="px-3" href="#testimonials">
          Testimonials
        </AnchorLink>
        <AnchorLink className="px-4" href="#market_analysis">
          Market Analysis
        </AnchorLink>   
        <Link className="px-3" to="/knowledge_center">
          Knowledge Center
        </Link>   
        <Link className="px-3" to="/qna/">
          Q & A
        </Link>                        
        <Link className="px-3" to="/about">
          About
        </Link>
      </div>
      <div className="hidden md:block">
        <Button className="text-sm">Start The Journey</Button>
      </div>
    </div>
  </header>
);

export default Header;
