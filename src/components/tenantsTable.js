import React, { useState, useEffect } from 'react';

function Tenants() {
  const [tenants, setTenants] = useState([]);

  useEffect(() => {
    // Fetch potential tenants from server
    // Update tenants state
  }, []);

  return (
    <div>
      <h2>Potential Tenants</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Contact Info (Facebook)</th>
            <th>Confidential Score</th>
            <th>Explanation</th>
          </tr>
        </thead>
        <tbody>
          {tenants.map((tenant, index) => (
            <tr key={index}>
              <td>{tenant.name}</td>
              <td><a href={tenant.facebookUrl}>Facebook Profile</a></td>
              <td>{tenant.confidentialScore}</td>
              <td>{tenant.explanation}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Tenants;
