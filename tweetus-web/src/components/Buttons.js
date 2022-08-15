import React from 'react'

function Button({action,style,tweet}) {
    const className = style ? style : 'btn btn-dark'
    let like =tweet.likes
    const actionsdisplay = action.display ? action.display : 'Action'
    const display =action.type === "Likes" ? `${like} ${actionsdisplay}` : `${actionsdisplay}`
    const handleonClick =(ev) =>{
      ev.preventDefault()
      if(action.type ==='Likes'){
        console.log(tweet.likes + 1)
        like=tweet.likes +1
      }
    }
    return (
   <button  className={className} onClick={handleonClick}>{display}</button>
    )
}

export default Button