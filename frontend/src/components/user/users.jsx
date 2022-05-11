import React, { Component, useEffect } from "react";
import { connect, connectAdvanced } from "react-redux";
import { getLeads } from "../../actions/leads";
import PropTypes from "prop-types";
// import leads from "../../reducers/leads";

export class Users extends Component {
  static propTypes = {
    leads: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.getLeads();
  };


  render() {
    return (
      <div className="container">
        {
            this.props.leads.map((item , index)=>(
                <div key={index}>
                    <p className="load">{item.name}</p>
                    
                </div>
            ))
        }
      </div>
    );
  }
}
const mapStateToProps = state => ({
  leads: state.leads.leads,
});

export default connect(mapStateToProps, { getLeads })(Users);

// const Users = (props) => {

//     useEffect(() => {
//         getLeads()
//         console.log(props);
//     }, []);

//     return (
//         <div>
//             this is users

//         </div>
//     );
// }

// const mapStateToProps = state => ({
//     leads: state.leads.leads
// })

// export default connect(mapStateToProps , {getLeads}) (Users);
