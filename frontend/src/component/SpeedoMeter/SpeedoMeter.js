import React, { PureComponent, Fragment } from 'react';
import './styles.css';


class SpeedoMeter extends PureComponent {


    
    constructor(props) {
        super(props);
        this.state = { neddleAngle: 227, scoreHealth: '' }; 
        this.adjustNeedlePosition = this.adjustNeedlePosition.bind(this);
        this.renderHealth = this.renderHealth.bind(this);
    }

    adjustNeedlePosition() {
        let value = this.props.score;
        let correctStartValue = value - this.props.startValue;
        let percent = ((correctStartValue * 100) / (this.props.endValue- this.props.startValue));
        let angle = (230 + ((percent * 180) / 100));
        this.setState({ neddleAngle: angle });
    }

    renderHealth() {
        let val = this.props.score;

        if (val <= this.props.healthCriteria[0]) {
            return "Bad"
        }
        else if (val <= this.props.healthCriteria[1] && val >= this.props.healthCriteria[0]) {
            return "Normal"
        }
        else if (val <= this.props.healthCriteria[2] && val >= this.props.healthCriteria[1]) {
            return "Good"
        }
    }

    render() {
        this.adjustNeedlePosition();
        let idStyle = "wrapper"
        if(this.props.isWealthResult === true)
        {
            idStyle = "wrapperForWealth";
        }
       
        return (
            <Fragment>
                <div id ={idStyle}>
                    
                
                       {
                           
                          <svg id="meter">       
                            <circle id="low" r="100" cx="50%" cy="50%" stroke="#FD6C34"
                                strokeWidth="50" strokeDasharray="314, 628" fill="none">
                            </circle>
                            <circle id="avg" r="100" cx="50%" cy="50%" stroke="#F8D200"
                                strokeWidth="50" strokeDasharray="211, 628" fill="none">
                            </circle>
                            <circle id="high" r="100" cx="50%" cy="50%" stroke="#09C199"
                                strokeWidth="50" strokeDasharray="120, 628" fill="none">
                            </circle>
                      </svg>

                    }
					   
                  
                    <img id="meter_needle" className="meter_needle" src={require('../../images/path2.png')} style={{ transform: 'rotate(' + this.state.neddleAngle + "deg)" }} alt="neddle" />
                    <div className="indicators">
                    <div className="labels">
                   
                    <div className="centerLabel" >{this.props.score}<div className="yourScore"> {this.renderHealth()}</div></div>
                    
                    </div>

                    </div>
                </div>
            </Fragment>
        )
    }


}

export default SpeedoMeter;

// <div className="sideLabel">{this.props.startValue}</div>
// <div className="sideLabel">{this.props.endValue}</div>