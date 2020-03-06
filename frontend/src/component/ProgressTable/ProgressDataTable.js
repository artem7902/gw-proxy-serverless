import React from 'react'
import {TableContainer,TableHead, TableRow, Table, TableBody, TableCell, Grid  } from '@material-ui/core'
import '../common.css'

  
  
function createData(prgectCode, prgectName, clientowner, clientName, netRev, PerTGT) {
    return {prgectCode, prgectName, clientowner, clientName, netRev, PerTGT};
  }
  
  const rows = [
    createData(1001, "Project1"),
    createData(1002, "Project2"),
    createData(1003, "Project3"),
    createData(1004, "Project4"),
    createData(1005, "Project5"),
    createData(1006, "Project6"),
    createData(1007, "Project7"),
    createData(1007, "Project8")
  ];
class DataTable extends React.Component{
    
   render(){
    return(
        <React.Fragment>              
          <TableContainer>          
          <h2>Top 10 Projects</h2>
          <Table aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell align="center">Project Code </TableCell>
                <TableCell align="center">Project Name</TableCell>
                <TableCell align="center">Client Owner</TableCell>
                <TableCell align="center">Client Name</TableCell>
                <TableCell align="center">Net Rev YTD</TableCell>
                <TableCell align="center">% TGT</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {rows.map(row => (
                <TableRow>
                  <TableCell align="center">{row.prgectCode}</TableCell>
                  <TableCell align="center">{row.prgectName}</TableCell>
                  <TableCell align="center">{row.clientowner}</TableCell>
                  <TableCell align="center">{row.clientName}</TableCell>
                  <TableCell align="center">{row.netRev}</TableCell>
                  <TableCell align="center">{row.PerTGT}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
        <Grid container>
          <Grid item xs={12}>
                <div className="sub-total-data">
                  <strong>Top Ten Subtotal = </strong><span>______________________</span>
                </div>
                <div className="sub-total-data">
                  <strong>All Clients Total = </strong><span>_______________________</span>
                </div>
          </Grid>
        </Grid>
        </React.Fragment>
    )

   }   
}
export default DataTable