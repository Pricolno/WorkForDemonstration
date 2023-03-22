import React from 'react';
import './App.css' 
import { Button } from './components/Button/Button';
import {Input} from './components/Input/Input';
import { Link } from './components/Link/Link';

import googleIcon from './images/google_icon.png'


export function App() {
  return (
   <div className="window-wrapper">
      <div className="img-left">
      </div>

      <div className="login">
        <div className="content-wrapper">
          <p className="welcome">
            Welcome back
          </p>
          <h1 className="title">
            Login to your account
          </h1>

        <form className="form" target="_blank">
          <Input text={'Email'} type={'email'} nameId={'email'} placeholder={'Email'}/>
          <Input text={'Password'} type={'password'} nameId={'password'} placeholder={'Password'} last/>


          <div className="remember-password">
            <div>
              <input type="checkbox" name="remember" className="remember-link" />
              <label>Remember me</label>
            </div>

            <Link text={'Forgot password?'} href={'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}/>
            
          </div>

          <div className="button-login-wrapper">
            <Button
            onClick={() => window.open('https\:\/\/www.youtube.com\/watch?v=dQw4w9WgXcQ')}
            classButton={'button-login'}
            text={'Login now'}
            />

          <Button
           onClick={() => window.open('https\:\/\/www.youtube.com\/watch?v=dQw4w9WgXcQ')}
           classButton={'button-login google'}
           text={
            <>
              <img src={googleIcon} alt={'google_icon'}></img>
              Or sign-in with google
            </>}
          />

          </div>
        </form>


        <div className="footer">
          <div className="footer-text">
            Dont have an account?
          </div>
          
          <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" className="join-us-link">
            Join free today
          </a>
        </div>

        
        </div>
      </div>
   </div>
  );
}


