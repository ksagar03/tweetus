import React from 'react'

const Tweets = ({tweet,className},props) => {
    // const className=  props.className ?props.className  : 'col-10 mx-auto col-md-6' if props is 
    // used then we need to specify like above 
    const className_ =  className? className: "col-10 mx-auto col-md-6"  // if any classname is not specfied the  
  return (
    <div className={className_}>{tweet.id} -
      {tweet.content}
    </div>
  )
}

export default Tweets
