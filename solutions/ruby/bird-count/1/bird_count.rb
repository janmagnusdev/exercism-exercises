class BirdCount
  def self.last_week
    return [0, 2, 5, 3, 7, 8, 4]
  end

  def initialize(birds_per_day)
    @this_week = birds_per_day
  end

  def yesterday
    return @this_week[-2]
  end

  def total
    return @this_week.sum
  end

  def busy_days
    debug "this week: #{@this_week}"
    return @this_week.reduce(0) do |sum, curr|
      next sum += 1 if curr >= 5
      sum
    end
  end

  def day_without_birds?
    return @this_week.count {|number| number == 0} > 0
  end
end
