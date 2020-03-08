import React, {Component} from 'react'



class Notes extends Component{   
    render(){
        return (
            <React.Fragment>
                <div className="notes-container">
                    <h3>{this.props.title}</h3>
                    <ul>
                        <li> </li>
                        <li> </li>
                        <li> </li>
                        <li> </li>
                        <li> </li>
                    </ul>
                </div>
            </React.Fragment>
        
        )
    }
  
}
export default Notes
