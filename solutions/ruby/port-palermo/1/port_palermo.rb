module Port
  IDENTIFIER = :PALE

  def self.get_identifier(city)
    value = city[0..3].upcase
    return value.to_sym
    
  end

  def self.get_terminal(ship_identifier)
    cargo = ship_identifier.to_s[0..2]
    unless cargo == "OIL" or cargo == "GAS"
      return "B".to_sym
    else 
      return "A".to_sym
    end
  end
end
