import React, { useState } from 'react';

function Input() {
  const [formData, setFormData] = useState({
    name: '',
    price: '',
    address: '',
    description: '',
    floorPlans: '',
    parkingPolicy: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = () => {
    // Send formData to server
    // Handle saving data and fetching potential tenants
  };

  return (
    <div>
      <h2>Input Details</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" placeholder="Name" value={formData.name} onChange={handleChange} />
        <input type="text" name="price" placeholder="Price" value={formData.price} onChange={handleChange} />
        <input type="text" name="address" placeholder="Address" value={formData.address} onChange={handleChange} />
        <textarea name="description" placeholder="Description" value={formData.description} onChange={handleChange} />
        <input type="text" name="floorPlans" placeholder="Floor Plans" value={formData.floorPlans} onChange={handleChange} />
        <input type="text" name="parkingPolicy" placeholder="Parking Policy" value={formData.parkingPolicy} onChange={handleChange} />
        <button type="submit">Save</button>
      </form>
    </div>
  );
}

export default Input;
