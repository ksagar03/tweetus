import React from 'react'

function Button({action,style,tweet}) {
    const className = style ? style : 'btn btn-dark'
  return (
   action.type === "Likes" ? <button  className={className}>{tweet.likes} {action.type}</button> : null
    )
}

export default Button