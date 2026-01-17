class LogLineParser
  def initialize(line)
    @line = line
  end

  def message
    left_strip = @line.index("[")
    right_strip = @line.index(":") + 1
    message = @line.dup
    message[left_strip..right_strip] = ""
    return message.strip
  end

  def log_level
    level = @line.dup
    left = level.index("[") + 1
    right = level.index("]") - 1
    return level.slice(left, right).downcase
  end

  def reformat
    message = self.message
    log_level = self.log_level
    return "#{message} (#{log_level})"
  end
end
