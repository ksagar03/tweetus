import React from 'react'
import Button from './Buttons'



// *************************************NOTE***************************************************
// We require(actionbtn) for each tweet so we imported 
// button.js(in this we have defined how a button should look and also further we will define 
// actions(functionallity))



const Tweets = ({tweet,className},props) => {
    // const className=  props.className ?props.className  : 'col-10 mx-auto col-md-6' if props is 
    // used then we need to specify like above 
    const className_ =  className? className: "col-10 mx-auto col-md-6"  // if any classname is not specfied the  
  return (
    <div className={className_}>{tweet.id} -
      {tweet.content}
      <div>
      <Button tweet={tweet} action={{type:"Likes",display:"Likes"}} style={"btn btn-dark"}/>
      <Button tweet={tweet} action={{type:"Unlike",display:"Unlike"}} style={"btn btn-dark"}/>
      <Button tweet={tweet} action={{type:"Retweet",display:"Retweet"}} style={"btn btn-dark"}/>
      </div>
    </div>


  )
}

export default Tweets
