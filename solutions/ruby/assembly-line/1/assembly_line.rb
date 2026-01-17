class AssemblyLine

  
  def initialize(speed)
    @speed = speed
    @CARS_PER_HOUR = 221
  end

  def production_rate_per_hour
    if @speed.between?(0, 4)
      success = 1.0
    elsif @speed.between?(5, 8)
      success = 0.9
    elsif @speed == 9
      success = 0.8
    elsif @speed == 10
      success = 0.77
    else 
      raise "Speed must be between 0 and 10"
    end
    return @speed * success * @CARS_PER_HOUR
  end

  def working_items_per_minute
    return (self.production_rate_per_hour / 60).floor
  end
end
